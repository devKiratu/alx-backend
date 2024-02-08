import { createClient } from 'redis';
import { promisify } from 'util';
import { createQueue } from 'kue';
import Express from 'express';

const app = Express();

const queue = createQueue();

const redisClient = createClient();
const AVALIALBLE_SEATS_KEY = 'available_seats';
let reservationEnabled = true;

redisClient.on('ready', () => {
  redisClient.set(AVALIALBLE_SEATS_KEY, 50);
});

function reserveSeat (number) {
  redisClient.set(AVALIALBLE_SEATS_KEY, number);
}

async function getCurrentAvailableSeats () {
  const getAsync = promisify(redisClient.get).bind(redisClient);
  return await getAsync(AVALIALBLE_SEATS_KEY);
}

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }
  const job = queue.createJob('reserve_seat', {}).save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    } else {
      return res.json({ status: 'Reservation in process' });
    }
  });
  job.on('complete', (result) => {
    console.log(`Seat reservation job ${job.id} completed`);
  });
  job.on('failed', (errMsg) => {
    console.log(`Seat reservation job ${job.id} failed: ${errMsg}`);
  });
});

app.get('/process', (req, res) => {
  queue.process('reserve_seat', async (job, done) => {
    const availableSeats = await getCurrentAvailableSeats();
    const newSeats = availableSeats - 1;
    if (newSeats === 0) reservationEnabled = false;
    if (newSeats >= 0) {
      reserveSeat(newSeats);
    } else {
      return done(new Error('Not enough seats available'));
    }
    done();
  });
  return res.json({ status: 'Queue processing' });
});

app.listen(1245);

export default app;
