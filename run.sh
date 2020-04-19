conda env create -f local_evn.yaml
conda activate covidqa
scrapy runspider covid_qa_spider.py -o who_covid_19_qa.csv
python gen_embedding.py
env FLASK_APP=serving.py flask run
