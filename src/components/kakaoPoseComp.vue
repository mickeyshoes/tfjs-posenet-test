<template>
    <div>
        <img id="test1" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaOWrLTrJPyiNCDym3-R6pKOWUTb-gaWQyLw&usqp=CAU" />
        <img id="test2" src="data:image/jpeg;base64,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" />
        <button @click="calculate">Request</button>
        
    </div>
</template>
<script>
import { reactive } from 'vue';
import _axios from '@/plugins/axios';

export default {

    methods: {

        async calculate(){

            const imageElement1 = document.getElementById('test1').src;
            const imageElement2 = document.getElementById('test2').src;

            Promise.all([
                this.requestKakaoAPI(imageElement1),
                this.requestKakaoAPI(imageElement2)

            ]).then(async poses => {

                console.log(poses);

            });


        },

        async requestKakaoAPI(image_url){
            let url = this.proxy_url+this.kakao_url+'/pose';
            // let url = this.kakao_url+'/pose';
            let config = {
                headers : {
                    "Authorization" : 'KakaoAK '+ this.api_key,
                    "Content-Type" : "application/x-www-form-urlencoded",
                },
                method: "POST",
                image_url: image_url,
            }

            const result = await _axios(url, config);
            console.log(result);
        },
    },

    setup() {
        
        const state = reactive({
            api_key : '31906a86d3468b6690dfd2ce4cffcefb',
            kakao_url: 'http://cv-api.kakaobrain.com',
            proxy_url : 'https://cors-anywhere.herokuapp.com/',
        });


        return{
            ...state,
        }

    }
    
}
</script>
<style>
    
</style>