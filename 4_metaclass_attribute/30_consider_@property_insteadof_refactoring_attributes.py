
import datetime
class Bucket(object):
    def __init__(self, period):
        self.period_delta = datetime.timedelta(seconds=period)
        self.reset_time = datetime.datetime.now()
        self.quota = 0
    
    def __repr__(self):
        return 'Bucket(quota=%d)' % self.quota
    
def fill(bucket, amount):
    now = datetime.datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amount

def deduct(bucket, amount):
    now = datetime.datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        return False
    if bucket.quota - amount < 0:
        return False
    bucket.quota -= amount
    return True

bucket = Bucket(60)
fill(bucket, 100)
print(bucket)
# >>>
# Bucket(quota=100)


if deduct(bucket, 99):
    print('Had 99 quota')
else:
    print('Not enough for 99 quota')
print(bucket)
# >>>
# Had 99 quota
# Bucket(quota=1)

if deduct(bucket, 3):
    print('Had 3 quota')
else:
    print('Not enough for 3 quota')
print(bucket)
# >>>
# Not enough for 3 quota
# Bucket(quota=1)


class Bucket(object):
    def __init__(self, period):
        self.period_delta = datetime.timedelta(seconds=period)
        self.reset_time = datetime.datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0
    
    def __repr__(self):
        return ('Bucket(max_quota=%d, quota_consumed=%d)' % 
            (self.max_quota, self.quota_consumed))
    
    @property
    def quota(self):
        return self.max_quota - self.quota_consumed
    
    @quota.setter
    def quota(self, amount):
        delta = self.max_quota - amount

        if amount == 0:
            # reset to new period
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            # fill quote of new period
            assert self.quota_consumed == 0
            self.max_quota = amount
        else:
            # consume quota during period
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta

bucket = Bucket(60)
print('Initial', bucket)
fill(bucket, 100)
print('Filled', bucket)

if deduct(bucket, 99):
    print('Had 99 quota')
else:
    print('Not enough for 99 quota')

print('Now', bucket)

if deduct(bucket, 3):
    print('Had 3 quota')
else:
    print('Not enough for 3 quota')
print('Still', bucket)
# >>>
# ('Initial', Bucket(max_quota=0, quota_consumed=0))
# ('Filled', Bucket(max_quota=100, quota_consumed=0))
# Had 99 quota
# ('Now', Bucket(max_quota=100, quota_consumed=99))
# Not enough for 3 quota
# ('Still', Bucket(max_quota=100, quota_consumed=99))