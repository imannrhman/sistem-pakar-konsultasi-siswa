<template>
<div class="flex flex-col">
  <div class="overflow-auto sm:-mx-6 lg:-mx-8">
    <div class="py-2 inline-block min-w-full max-h-screen sm:px-6 lg:px-8">
      <div class="overflow-hidden">
        <table :key="index" v-for="(result, index) in results" class="mb-5">
          <tbody>
            <tr>
              <th class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">Behavior</th>
              <td class="align-bottom text-sm text-gray-900 font-bold px-6 py-4 whitespace-nowrap text-ellipsis">
                {{result.behavior}}
              </td>
            </tr>
            <tr class="bg-white">
              <th class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">Masalah</th>
              <td :key="index" v-for="(solution, index) in result.solutions" class="align-bottom text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap text-ellipsis ">
                        {{solution.text}}
              </td>
            </tr>
            <tr class="bg-white">
              <th class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">Solusi</th>
              <td :key="index" v-for="(problem, index) in result.problems" class="align-bottom text-sm text-gray-900 font-light px-6 py-4 text-ellipsis">
                   {{problem.text}}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</div>
</template>
<script>
export default {
        props: {
        results: {
            type: Array,
            required: true,
        },
    },        
}
</script>>