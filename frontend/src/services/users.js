import { api } from 'src/boot/axios'

export default {
  getById(id) {
    return api.get(`/users/${id}`)
  }
}