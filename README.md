# Example scripts to interact with desire6g-test-component

First make sure to spawn a rabbitmq instance. EG:

```
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

Then instantiate the desire6g-test-component:

```
git clone https://github.com/nubispc/desire6g-test-component
cd desire6g-test-component
export RABBITMQ_HOST=localhost
export INPUT_TOPIC="myinput"
export OUTPUT_TOPIC="myoutput"
python3 processor.py
```

On another terminal, do:

```
export OUTPUT_TOPIC="myoutput"
python3 subscribe.py
```

And on a third terminal do:

```
export INPUT_TOPIC="myinput"
python3 publish.py
```

You should be able to see:

```
$ python3 publish.py
Message published to queue 'myinput': {'example_key': 'example_value'}
```

```
$ python3 subscribe.py                    
Subscribed to queue 'myoutput'. Waiting for messages...                   
Received message from queue 'myoutput': {'example_key': 'example_value'}  
```

```
INFO:ProcessingSystems.rabbitmq:Processing message 1...
INFO:ProcessingSystems.rabbitmq:Received and processing YAML data:
INFO:ProcessingSystems.rabbitmq:{'example_key': 'example_value'}
INFO:ProcessingSystems.rabbitmq:Message 1 processing complete.
INFO:ProcessingSystems.rabbitmq:Processed message 1: {"example_key": "example_value"}
```
