# Set up VM Demo

## Packages
pip install pandas<br>
pip install matplotlib<br>
pip install pymongo<br>
pip install python-dotenv<br>
pip install psycopg2-binary<br>
pip install nest_asyncio<br>
pip install python-binance<br>

## Copy the folder Bot_binance on the VM
- Drag & drop the folder using Visual Studio
- Or manage SSH key on your VM and put public key on GitHub or simply
git clone git@github.com:FGaloha/binance_bot.git

## Create your api access on the testnet binance
https://testnet.binance.vision

## Check .env contains necessary variables
touch .env
- Add the following variables<br>
MONGO_USER=userAdmin<br>
MONGO_PWD=userPassword<br>
POSTGRES_USER=useradmin<br>
POSTGRES_PASSWORD=userpassword<br>
BTCUSDT_LIMIT= 28000<br>
API_KEY_TESTNET=REPLACE_BY_YOUR_KEY<br>
API_SECRET_TESTNET=REPLACE_BY_YOUR_SECRET<br>

- Generate from the terminal those used by airflow<br>
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" >> .env

## Be sure you have the rights
chmod +x setup.sh

## Run setup
./setup.sh

## Put the period in historical-data-engine.py
python3 -u historical-data-engine.py > results/engine.txt

## Actions to do from Airflow

Access airflow:
http://localhost:8080/

Run the DAG btc_market_analysis to:
- create & save machine learning models
- select the best one

Copy the best model to the bot api folder and reload the service:
cp dags/Random_Forest_model.pkl bot_api/
docker-compose build botapi
docker-compose up -d botapi

## Access Jupyter notebook

http://localhost:8888/

## To test the api put localhost or the IP of your VM
- Check running<br>
http://localhost:8000
- Check prediction<br>
http://localhost:8000/prediction?eur_avg=30000.1&usdc_avg=30000.1&dai_avg=30000.1&gbp_avg=30000.1

## Cronjobs on VM
* * * * * /usr/bin/python3 /home/ubuntu/binance_bot/call_bot_api.py >> /home/ubuntu/binance_bot/results/call_bot_api.json 2>&1

* * * * * /usr/bin/python3 /home/ubuntu/binance_bot/stream.py >> /home/ubuntu/binance_bot/results/stream_2.txt 2>&1

*** *** *** *** *** ***

# Used for tests only
- Uses a MongoDB market collection using historical-data-engine-FG.py (works also with historical-data-engine.py) and generating a machine learning model using service pyspark
- Models is copied on the bot_api at the end of the process and can be used by bot_apy.py

## To do only if the model does not already exist or need to be updated
- The COPY function does not work on the jupyter notebook image so it is managed after container creation<br>
docker cp ./pyspark/model-generation.py pyspark:/home/jovyan/model-generation.py

- generate model executing model-generation.py in pyspark container<br>
docker exec pyspark python /home/jovyan/model-generation.py

- copy model generated in pyspark container in botapi container<br>

  <b>VM</b><br>
docker cp pyspark:/home/jovyan/work/. jupyter_notebook_volume/<br>

  <b>MacOS</b><br>
docker cp pyspark:/home/jovyan/work/bot_api_model/ jupyter_notebook_volume/

## To do each time after docker-compose up -d
docker cp jupyter_notebook_volume/. botapi:/app/models/
