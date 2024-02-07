import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();
const asyncGet = promisify(client.get).bind(client);
const asyncSet = promisify(client.set).bind(client);

client
  .on('ready', () => console.log('Redis client connected to the server'))
  .on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

async function setNewSchool (schoolName, value) {
  const res = await asyncSet(schoolName, value);
  print(null, res);
}

async function displaySchoolValue (schoolName) {
  const reply = await asyncGet(schoolName);
  console.log(reply);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
