import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

const asyncGet = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  try {
    const value = await asyncGet(schoolName);
    console.log(`Value for ${schoolName}: ${value}`);
  } catch (err) {
    console.error(`Error retrieving value for ${schoolName}: ${err}`);
  }
}

async function execute() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

execute().catch((err) => {
  console.error('Error executing functions:', err);
});
