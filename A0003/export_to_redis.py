import redis
import sys
sys.path.append('..')
import A0001.Invente_card

REDIS_SAVE_KEY = 'codes'


def export_reids(server):
    print('start to export data to redis')
    [server.sadd(REDIS_SAVE_KEY, i) for i in A0001.Invente_card.generator()]


def get_data_from_redis(server):
    print(server.smembers(REDIS_SAVE_KEY))
    print(server.scard(REDIS_SAVE_KEY))


if __name__ == '__main__':
    redis_server = redis.Redis() # 全用默认配置
    redis_server.delete(REDIS_SAVE_KEY)
    export_reids(redis_server)
    get_data_from_redis(redis_server)