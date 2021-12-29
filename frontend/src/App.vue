<template>
  <Test v-if="!loading" :questions="questions"/>
   <div class="mt-40" v-if="loading">
      <p class="text-6xl font-bold text-center text-gray-500 animate-pulse">
        Loading...
      </p>
    </div>
</template>
<script>
import Test from './components/Test.vue'
import Layout from './components/Layout.vue'
import axios from "./plugins/axios"

export default {
  components: {
    Layout,
    Test,
  },
  data() {
    return {
      questions: [{}],
      loading: false,
      error: null,
    }
  },
  methods: {
     async fetchQuestions() {
          console.log('test')
          this.loading = true
            try {
                const { data } = await axios.get('/questions/')
                console.log(data)
                this.questions = data
                this.loading = false
            } catch (e) {
                console.log(e);
            }
          this.loading = false
        },
  },
  mounted() {
    this.fetchQuestions()
  },
}
</script>