const axios = require('axios')

const api_token = process.env.DATAROBOT_API_TOKEN
const username = process.env.DATAROBOT_API_USERNAME
const datarobot_key = process.env.DATAROBOT_API_KEY
const deployment_id = '5c51af53969ce00199d2c9dc'

let url = `https://datarobot-predictions.orm.datarobot.com/predApi/v1.0/deployments/${deployment_id}/predictions`
let auth = { username: username, password: api_token }

let headers = {
  'Content-Type': 'application/json; charset=UTF-8',
  'datarobot-key': datarobot_key
}

const data = [
  {
    "horsepower": 130,
    "weight": 3504,
    "displacement": 307,
    "cylinders": 8,
    "model year": 70,
    "origin": 1,
    "acceleration": 12
  },{
    "horsepower": 165,
    "weight": 3693,
    "displacement": 350,
    "cylinders": 8,
    "model year": 70,
    "origin": 1,
    "acceleration": 11.5
  }
]

console.log("DataRobot Request")
console.log(JSON.stringify(data, null, 2))
console.log()

axios.post(url, data, { headers, auth })
  .then(response => {
    console.log("DataRobot Response")
    console.log(JSON.stringify(response.data, null, 2))
    console.log()
  }).catch(error => {
    console.error(error)
  })
