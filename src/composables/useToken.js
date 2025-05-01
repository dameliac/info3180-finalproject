import { ref, watch } from 'vue'

const token = ref(localStorage.getItem('token'))

watch(token, (newToken) => {
    console.log("Changed")
  if (newToken) {
    localStorage.setItem('token', newToken)
  } else {
    localStorage.removeItem('token')
  }
})

export function useToken() {
  return { token }
}
