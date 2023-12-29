import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    queue = kue.createQueue({ redis: { createClientFactory: () => kue.redis.createClient } });
    queue.testMode.enter();
  });

  after(() => {
    queue.testMode.exit();
  });

  beforeEach(() => {
    queue.testMode.clear();
  });

  it('display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('invalid', queue)).to.throw('Jobs is not an array');
  });

  it('create two new jobs to the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 5678 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    const jobsInQueue = queue.testMode.jobs;

    expect(jobsInQueue.length).to.equal(2);

    expect(jobsInQueue[0].type).to.equal('push_notification_code_3');
    expect(jobsInQueue[0].data).to.eql(jobs[0]);

    expect(jobsInQueue[1].type).to.equal('push_notification_code_3');
    expect(jobsInQueue[1].data).to.eql(jobs[1]);
  });
});
