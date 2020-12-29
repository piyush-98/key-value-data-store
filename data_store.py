import json
import time
class database:
    def __init__(self,filepath=''):
        self.filepath=filepath
        self.df={}
        self.df_time_to_live={}
        print('''database instantiated on {} this path. 
        If you want to change this path provide a valid path as a parameter during the initialisation'''.format(filepath))

    def create(self,key,value,time_to_live=-1):
        if(key in self.df.keys()):
            raise Exception("key exists")
        else:
            self.df[key]=value
            create_time=time.time()
            self.df_time_to_live[key]={'timetolive':time_to_live,'createtime':create_time}

            self.save_db()
            self.save_time_db()

    def read(self,key):
        try:
            self.check_expiry(key)
            result = (self.df[key])
            print(result)
        except Exception as e:
            print("The key {} does not exist or it has expired".format(e))
    def delete(self,key):
        try:
            self.check_expiry(key)
            del self.df[key]
            del self.df_time_to_live[key]
            self.save_time_db()
            self.save_db()

        except Exception as e:
            print("The key {} does not exist or it has expired".format(e))

    def check_expiry(self,key):
            retained_time=self.df_time_to_live[key]['timetolive']
            if(retained_time!=-1):
                create_time=self.df_time_to_live[key]['createtime']
                current_time=time.time()
                if(current_time-create_time>retained_time):
                    del self.df[key]
                    del self.df_time_to_live[key]
                self.save_db()
                self.save_time_db()



    def show(self):
        print(self.df)

    def save_db(self):
        if(len(self.filepath)!=0):
            self.filepath=self.filepath+ '/'
        with open('{}data.json'.format(self.filepath), 'w') as fp:
            json.dump(self.df, fp)
    def save_time_db(self):
        with open('{}time.json'.format(self.filepath), 'w') as fp:
            json.dump(self.df_time_to_live, fp)
            



