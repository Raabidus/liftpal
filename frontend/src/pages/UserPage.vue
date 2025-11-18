<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import Users from 'src/services/users'

const route = useRoute()
const user = ref(null)

onMounted(() => {
  console.log('Fetching user:', route.params.id)
  Users.getById(route.params.id).then(res => {
    console.log('API response:', res.data)
    user.value = res.data
  })
})
</script>

<template>
  <q-page padding>
    <h4>User Detail Page</h4>

    <div v-if="user">
      <pre>{{ user }}</pre>
    </div>
    <div v-else>
      Loading...
    </div>
  </q-page>
</template>