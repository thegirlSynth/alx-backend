import kue from 'kue';

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    const errorMessage = `Phone number ${phoneNumber} is blacklisted`;
    job.failed(new Error(errorMessage));
    console.log(`Notification job ${job.id} failed: ${errorMessage}`);
    done(new Error(errorMessage));
  } else {
    job.progress(50, 100);

    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    setTimeout(() => {
      console.log(`Notification job ${job.id} completed`);
      job.complete();
      done();
    }, 1000);
  }
}

const queue = kue.createQueue({ concurrency: 2 });

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;

  sendNotification(phoneNumber, message, job, done);
});
