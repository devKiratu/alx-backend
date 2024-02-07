import { createClient } from 'redis';

const client = createClient();

client
  .on('ready', () => console.log('Redis client connected to the server'))
  .on('error', err => console.log('Redis client not connected to the server: ', err.message))
  .connect();
