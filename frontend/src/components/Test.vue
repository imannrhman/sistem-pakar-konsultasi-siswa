<template>
     <div class="flex items-center justify-center w-full h-screen" id="app">
            <div class="w-full max-w-fit max-h-screen">
                <h1 class="text-4xl font-bold text-center text-indigo-900">
                    Konsultasi Siswa
                </h1>
                <div class="w-max-full w-h-screen p-12 mt-8 bg-white rounded-lg shadow-lg">
                    <div v-if="index < questions.length" class="max-w-xl">
                        <p class="text-2xl font-bold">
                            {{ questions[index].code + ". " +questions[index].text }}
                        </p>
                        <label
                            :for="key"
                            class="block px-6 py-2 mt-5 text-lg border border-gray-300 rounded-lg"
                            v-for="answer,key in answers"
                            :class="{'hover:bg-gray-100 cursor-pointer' : selectedAnswer == ''},
                        {'bg-green-100  border border-10 border-green-400' : selectedAnswer == key && selectedAnswer != ''}"
                        >
                            <input
                                type="radio"
                                :id="key"
                                class="hidden"
                                :value="key"
                                @change="answered($event)"
                                v-model="selectedAnswer"
                            />
                            {{ answer.text }}
                        </label>
                        <div class="flow-root mt-6">
                            <button
                                class="float-right px-5 py-2 text-sm font-bold tracking-wide text-white bg-indigo-900 rounded-full"
                                v-show="selectedAnswer != '' && index <  questions.length - 1 "
                                @click="nextQuestion"
                            >
                                Selanjutnya &gt;
                            </button>
                            <button
                                class="float-right px-5 py-2 text-sm font-bold tracking-wide text-white bg-indigo-900 rounded-full"
                                v-show="selectedAnswer != '' && index ==  questions.length - 1"
                                @click="showResults"
                            >
                                Lihat Hasil
                            </button>
                        </div>
                    </div>
                    <div v-else>
                        <h2 class="text-3xl font-bold">Hasil Keputusan</h2>
                        <div class="justify-start">
                            <Result :results="results" />
                        </div>
                        <div class="flow-root mt-6 ">
                            <button
                                class="float-right px-5 py-2 text-sm font-bold tracking-wide text-white bg-indigo-900 rounded-full"
                                @click="resetQuiz"
                            >
                                Coba Lagi
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
</template>
<script>
import axios from "../plugins/axios"
import Result from "./Result.vue"

export default {
    components: {
        Result,
    },
    props: {
        questions: {
            type: Array,
            required: true,
        },
    },
    data() {
        return {
            index: 0,
            userAnswer:[],
            results : [],
            selectedAnswer: '',
            correctAnswer: 0,
            wrongAnswer: 0,
            answers : [
                {
                    text : 'Ya',
                    value : true,
                },
                {
                    text : 'Tidak',
                    value : false,
                },
                ],
        }
    },
    methods: {
        answered(e) {
            this.selectedAnswer = e.target.value
            if(this.answers[this.selectedAnswer].value)
                    this.userAnswer.push(this.questions[this.index].code)
            else
               if(this.userAnswer.includes(this.questions[this.index].code))
                    this.userAnswer.pop()
           
            console.log(this.userAnswer)
        },
        nextQuestion() {
            this.index++
            this.selectedAnswer = ''
        },
        async showResults() {
            try {
             const codes = {"codes" : this.userAnswer}
             const { data } = await axios.post('/questions/result', codes)
             this.results = data 
             this.index++   
            } catch(e) {
                console.log(e)
            }
        },
        resetQuiz() {
            this.index = 0
            this.selectedAnswer = ''
            this.userAnswer = []
        },
    },
  
}


</script>