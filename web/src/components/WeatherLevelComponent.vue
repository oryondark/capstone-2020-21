<template>
  <div class="inline-block" style="padding-bottom:20px">
    <b-img blank blank-color="white" :style="styles[0]"></b-img>
    <b-img blank blank-color="#87b0e6" :style="styles[1]"></b-img>
    <b-img blank blank-color="#d15664" :style="styles[2]"></b-img>
    <b-img blank blank-color="white" :style="styles[3]"></b-img>
  </div>
</template>

<script>
export default {
  props: [
    'index'
  ],
  computed: {
    styles: function () {
      if (1 <= this.index && this.index < 3) {
        return [
          { width: (this.index-1)*25 + '%', height: 1 + 'rem' },
          { width: 50-((this.index-1)*25) + '%', height: 1 + 'rem' },
          { width: 0 + '%', height: 1 + 'rem' },
          { width: 50 + '%', height: 1 + 'rem' }
        ]
      } else if (3 < this.index && this.index <= 5) {
        return [
          { width: 50 + '%', height: 1 + 'rem' },
          { width: 0 + '%', height: 1 + 'rem' },
          { width: ((this.index-1)*25-50) + '%', height: 1 + 'rem' },
          { width: 50-((this.index-1)*25-50) + '%', height: 1 + 'rem' }
        ]
      } else if (this.index === 3){
          return [
          { width: 40 + '%', height: 1 + 'rem' },
          { width: 10 + '%', height: 1 + 'rem' },
          { width: 10 + '%', height: 1 + 'rem' },
          { width: 40 + '%', height: 1 + 'rem' }
        ]
      } else {
        return [
          { width: 50 + '%', height: 1 + 'rem' },
          { width: 0 + '%', height: 1 + 'rem' },
          { width: 0 + '%', height: 1 + 'rem' },
          { width: 50 + '%', height: 1 + 'rem' }
        ]
      }
    }
  }
}
</script>
