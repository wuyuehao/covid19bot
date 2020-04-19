curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"utterances":[ "can I remove or replace my implant or IUD during COVID-19 pandemic?" ]}' \
  http://localhost:5000/predict


curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"utterances":[ "How are COVID-19 different from other viruses?" ]}' \
  http://localhost:5000/predict

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"utterances":[ "I am pregnant, am I at higher risk from COVID-19" ]}' \
  http://localhost:5000/predict

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"utterances":[ "What should I do if I think I have COVID-19" ]}' \
  http://localhost:5000/predict