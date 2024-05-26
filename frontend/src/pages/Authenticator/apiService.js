import { getHeaders } from '../../utils'
import axios from '../../utils/axios'


export const getAuthSecret = async () => {
  return await axios.get('/drf-2fa/get-auth-secret/', { headers: getHeaders()})
}
