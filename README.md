# key_val_data_store

This is my submission for the key value data store task in python.

Requirements

**Python**

Please clone this repository.

Change the working directory to the cloned repository. You can run all of the python commands given below to use the data store.

Open a python file or directly run these commands from python command line.

import the database from data_store. 

`from data_store import database`

`db=database()`

Initialise the database object, you can pass the file path to store the database as a parameter during the initialisation.

`db=database(r'C:\Users\PIYUSH\Desktop')`

Please use *r* before the file path.

By default the database will be stored in the working directory itself.

**create()**

The create() will take three arguments.
key - a string value
value - a json object/string
time_to_live- an integer defining the number of seconds a key must be retained the default value is -1 which signifies that there is no time to live property for the given key.

`db.create('foo',{1:"1",2:"2"},-1)`

`db.create('bar',{1:"1",2:"2"},10)`

**read()**

The read() will take the key as an argument. It prints the json value for a key.

`db.read('foo')`

**delete()**

The delete() will take the key as an argument. it deletes the given key value pair.

`db.delete('foo')`

**show()**

It takes no argument and shows the data.

`db.shows()`

I have used the time stamps for the time to live property, hence right now a key gets expired only if we try to explicitly call the read() or delete().
The moment we run a read or delete command on a key the code will check that the key is expired and if it is expired it will delete the key and the key doesn't exist message will be returned.

We can also set up a cron job for this task which can implicitly do the job for us like a scheduled task.



