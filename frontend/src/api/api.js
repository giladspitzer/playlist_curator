import axios from 'axios'
// const host = location.hostname
 axios.defaults.baseURL = 'http://localhost:5000';

const apiCall = (method, path, payload=null) => {
    return new Promise((resolve, reject) => {
        axios.request({
            method: method,
            url: path,
            data: payload
        })
        .then(resp => {
            resolve(resp)
        })
        .catch(err => {
            console.warn(err)
            reject(err)
        })
    })
}

export const getPlaylists = () => {
    return apiCall('get', '/api/playlists')
}
