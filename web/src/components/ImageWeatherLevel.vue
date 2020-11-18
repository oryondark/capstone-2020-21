<template>
  <b-container style="border:1px solid #17A2B8;background-clip:content-box">
    <br>
    <b-col>
      <b-row class="justify-content-center mb-3">
        <h6>날씨 적절성</h6>
      </b-row>
      <p class="m-auto w-75" v-if=this.show><WeatherLevelComponent :index="weather_level" /></p>
      <b-row class="justify-content-center mb-3">{{this.level_text}}</b-row>
    </b-col>
  </b-container>
</template>

<script>
import axios from 'axios'
import consts from '@/consts.js'
import WeatherLevelComponent from '@/components/WeatherLevelComponent.vue'

export default {
  components: {
    WeatherLevelComponent
  },
  props: [
    'codyId'
  ],
  data: function () {
    return {
      weather_level: '',
      level_text: '',
      show: ''
    }
  },
  created: function () {
    // get weatherlevel
    var token = window.localStorage.getItem('token')
    var config = {
      headers: { Authorization: `Bearer ${token}` }
    }
    var data = {
      clothes_set_id: this.codyId,
      maxTemp: window.localStorage.getItem('localMaxTemp'),
      minTemp: window.localStorage.getItem('localMinTemp'),
      windSpeed: window.localStorage.getItem('localWindSpeed'),
      humidity: window.localStorage.getItem('localHumidity')
    }
    axios.post(`${consts.SERVER_BASE_URL}/clothes-set-reviews/today_cody_review/`, data, config)
      .then(response => {
        this.weather_level = response.data.predict
        this.show = true
        if (Math.round(this.weather_level) === 1) { this.level_text = '오늘 날씨에 매우 춥습니다.'}
        else if (Math.round(this.weather_level) === 2) { this.level_text = '오늘 날씨에 조금 춥습니다.'}
        else if (Math.round(this.weather_level) === 3) { this.level_text = '오늘 날씨에 적당합니다.'}
        else if (Math.round(this.weather_level) === 4) { this.level_text = '오늘 날씨에 조금 덥습니다.'}
        else if (Math.round(this.weather_level) === 5) { this.level_text = '오늘 날씨에 매우 덥습니다.'}
        else if (this.weather_level === -1) {
          this.level_text = '오늘 날씨와 유사한 날씨에 입은 코디 리뷰가 없습니다.'
          this.show = false
        } else if (this.weather_level === -2) {
          this.level_text = '해당 코디에 대한 리뷰가 존재하지 않습니다.'
          this.show = false
        } else {
          this.level_text = '오류입니다.'
          this.show = false
        }
      }).catch(ex => {
        this.level_text = '날씨를 불러오지 못했습니다.'
      })
  }
}
</script>
