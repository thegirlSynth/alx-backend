import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a notification message.',
};

const job = queue.create('push_notification_code', jobData);

job.on('enqueue', (id, type) => {
  console.log(`Notification job created: ${id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});

job.save((err) => {
  if (err) {
    console.error(`Error creating job: ${err}`);
  } else {
    console.log('Job saved to the queue');
    process.exit(0);
  }
});
