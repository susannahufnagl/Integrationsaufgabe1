<template>
    <div id="account">
        <h1>Erstelle deinen Account</h1>
        <div class="AccountErstellen">
            <input type="text" v-model="vorname" placeholder="Enter Vorname"/>
            <input type="text" v-model="nachname" placeholder="Enter Nachname"/>
            <input type="number" v-model="alter" placeholder="Enter Alter"/>
            <div v-if="alter && alter < 1">Gültiges Alter eingeben</div>
            <div v-if="alter && alter < 18">Warte bis du 18 bist!</div>
            <input type="email" v-model="email" placeholder="Enter Email"/>
            <select v-model="wählbar" required>
                <option disabled value="Bitte auswählen"></option>
                <option value="wählbar">wählbar</option>
                <option value="nicht wählbar">nicht wählbar</option>
            </select>
            <button @click="createPerson">createPerson</button>
                <p v-if="submitted">submitted</p> <!-- api an server schicken dass account erstellt wird-->
           

            <router-link to="`/wahlen/`">Zu den Wahlen</router-link>
        </div>
    
    </div>

</template>
<script>
import axios from 'axios';
import { mapActions } from 'vuex'; 
export default{
    name: 'AccountErstellen',
    data(){
        return{
            vorname: '',
            nachname: '',
            alter: null,
            email:'',
            wählbar:'',
            gewähltePerson: null,
            submitted:false,

        }
    },
    methods:{
        ...mapActions(['addPerson']),
        createPerson(){
            if(this.alter < 1 ){
            alert("Gültiges Alter eingeben!");}
            else if(this.alter< 18){
                alert("Warte bis du 18 bist!")
            }else {
            

            axios.post('http://localhost:8081/persons',{
                vorname: this.vorname,
                nachname: this.nachname,
                alter:this.alter,
                email:this.email,
                wählbar:this.wählbar,
        })
        .then(response=>{
            console.log(response);
            this.gewähltePerson= response.data;
            this.submitted=true;
            this.addPerson(response.data);
            this.$router.push("/wahlformular");
        })
        .catch((error)=>{
            console.log(error);
        });
            }
        },
    },
};

    

</script>