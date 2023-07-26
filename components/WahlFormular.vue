<template>
    <div id="wahlen">
        <h1>Wähle hier deine Kandidat:innen des Vertrauens aus</h1>
        <div class="WahlFormular">
            <div v-for="person in kandidaten" :key="person.id">
                <input type="radio" v-model="gewählteperson" :value="person" />
                {{ person.vorname }} {{ person.nachname }}
                </div>

            
           
            <button @click="wählen">Wählen</button>
        </div>
    
    </div>
</template>
<script>

import axios from 'axios';
import { mapGetters } from 'vuex';
export default{
    name:'WahlFormular',
    computed:{
        ...mapGetters(['kandidaten'])
        
    },
    data(){
        return{
            
            gewählteperson: null,
            

        }
    },
    
    methods:{
        wählen(){

            axios.post('http://localhost:8081/vote',{
                vorname: this.$store.state.user.vorname,
                nachname: this.$store.state.user.nachname,
                gewählteperson:this.gewählteperson.id
        })
        .then(response=>{
            console.log(response);
        })
        .catch(error=>{
            console.log(error);
        });
    }
    },
    mounted(){
        
        axios.get('http://localhost:8081/vote')
        this.$store.dispatch('zuwählende')
        .then(response => {
            this.kandidaten= response.data.filter(person=> person.wählbar== "wählbar");
        })
        .catch(error=> {
            console.log(error);
        })
    }
}
</script>