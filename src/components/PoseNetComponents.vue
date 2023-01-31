<template>
    <div>
        <h2>pose estimation demo</h2>
        <img id="test1" width="250" height="250" src="data:image/jpeg;base64,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"/>
        <!-- <img id="test2" src="data:image/jpeg;base64,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"/> -->
        <img id="test3" width="250" height="250" src="data:image/jpeg;base64,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"/>
        <!-- {{ pose }} -->
        <button @click="calPose">get pose</button>

        {{ resultMsg }}

    </div>
</template>
<script>
import { reactive } from 'vue';
import { poseSimilarity } from 'posenet-similarity';
import * as tf from '@tensorflow/tfjs-core';
import '@tensorflow/tfjs-backend-cpu';
import * as posenet from '@tensorflow-models/posenet';

export default {

    methods: {

        async loadModel(){
            this.net = await posenet.load();

            return this.net? true:false;
        }, 

        async estimate(imageElement, modelConfig){
            this.net = await posenet.load(modelConfig);
            console.log(this.net);
            // console.log(imageElement.src);
            var startInference = Date.now();
            const pose = await this.net.estimateSinglePose(imageElement, 0.5, this.flipHorizontal, this.outputStride);
            console.log('inf time : ', Math.floor((Date.now() - startInference)/1000));
            return pose;
        },

        async calSimilarity(config, origin, target){

            var calStartTime = Date.now();
            const similarity = await poseSimilarity(origin, target, config);
            var calEndTime = Date.now();
            let strategy = config.strategy;

            return {strategy : strategy, result : similarity, time : Math.floor((calEndTime - calStartTime)/1000)};
        },

        serializeObject(object){
            return JSON.stringify(object);
        },

        async calPose(){
            const pose1Image = document.getElementById('test1');
            const pose2Image = document.getElementById('test3');
            var startInference = Date.now();
            // this.net = await posenet.load();
            Promise.all([
                this.estimate(pose1Image, {architecture : "MobileNetV1", multiplier: 0.5}),
                this.estimate(pose2Image, {architecture : "MobileNetV1"})
            ]).then(poses => {
                console.log('inf time : ', Math.floor((Date.now() - startInference)/1000));
                
                startInference = Date.now();
                const weightedDistance = poseSimilarity(poses[0], poses[1], {strategy: 'weightedDistance'});
                console.log('inf time for similarity: ', Math.floor((Date.now() - startInference)/1000));
                console.log('Weight Distance : ', weightedDistance);
                
                
                startInference = Date.now();
                const cosineDistance = poseSimilarity(poses[0], poses[1], {strategy: 'cosineDistance'});
                console.log('inf time for similarity: ', Math.floor((Date.now() - startInference)/1000));
                console.log('Cosine Distance : ', cosineDistance);
                
                
                startInference = Date.now();
                const cosineSimilarity = poseSimilarity(poses[0], poses[1], {strategy: 'cosineSimilarity'});
                console.log('inf time for similarity: ', Math.floor((Date.now() - startInference)/1000));
                console.log('Cosine similarity : ', cosineSimilarity);
            });
        }
    },

    setup() {
        const state = reactive({
            net: '',
            imageScaleFactor: 0.5,
            flipHorizontal: false,
            outputStride: 16,
            resultMsg: "",
        });

        console.log(tf.getBackend());

        // this.loadModel();

        return {
            ...state,
        }
    }
    
}
</script>
<style lang="">
    
</style>