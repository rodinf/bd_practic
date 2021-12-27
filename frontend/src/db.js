import axios from 'axios'

class DBApi {
  constructor(proto, host, port, dir) {
    this.proto = proto
    this.host = host
    this.port = port
    this.dir = dir
  }
  fetchAll() {
    axios
      .get(this.proto + "://" + this.host + ":" + this.port + "/" + this.dir)
      .then((response) => {
        console.log(response.data)
      })
      .catch((error) => {
        console.log(error)
      })
  }
}

export default DBApi