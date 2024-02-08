import { createQueue } from 'kue';
import { expect } from 'chai';
import { before, afterEach, after, beforeEach } from 'mocha';
import { spy} from 'sinon'

import createPushNotificationsJobs from './8-job';

const queue = createQueue();

describe( 'test suite for createPushNotificationsJobs', () => {
  let consoleSpy;
  before( () => {
    queue.testMode.enter()
  } )

  beforeEach( () => {
    consoleSpy = spy(console, 'log')
  })
  
  afterEach( () => {
    queue.testMode.clear()
    consoleSpy.restore()
  } )
  
  after( () => {
    queue.testMode.exit()
  } )
  
  it( 'should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('', queue)).to.throw('Jobs is not an array')
  } )
  
  // it( 'should log Notification job created: JOB_ID when a job is created', () => {
  //   const jobs = [ {
  //     phoneNumber: '12345',
  //     message: 'hello world'
  //   } ]
  //   createPushNotificationsJobs( jobs, queue );
  //   expect( queue.testMode.jobs.length).to.equal(1);
  // })
})
