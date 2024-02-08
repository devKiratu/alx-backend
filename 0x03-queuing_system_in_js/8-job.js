export default function createPushNotificationsJobs (jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobData) => {
    const job = queue.createJob('push_notification_code_3', jobData).save((err) => {
      if (!err) console.log(`Notification job created: ${job.id}`);
    });

    job.on('complete', (result) => {
      console.log(`Notification job ${job.id} completed`);
    });

    job.on('failed', (errorMsg) => {
      console.log(`Notification job ${job.id} failed: ${errorMsg}`);
    });

    job.on('progress', (progress, data) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}
