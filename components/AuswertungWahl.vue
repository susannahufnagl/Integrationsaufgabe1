<template>
    <div id="auswerten">
        <h1>Wahlergebnisse</h1>
        <div class="AuswertungWahl">
        <table>
            <thead>
                <tr>
                    <th>vorname nachname</th>
                    <th>stimmen</th>
                    <th>prozent</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(Kandidat, index) in $store.state.results" :key="index">
                <td>{{ Kandidat.vorname }} {{ Kandidat.nachname }}</td>
                <td>{{ Kandidat.stimmen }}</td>
                <td>{{ Kandidat.prozent }}%</td>

                </tr>
            </tbody>
        </table>
    </div>
        
    </div>

</template>
<script>


export default{

    name:'AuswertungWahl',
    mounted(){
      this.$store.commit('berechne');
    }
  }
</script>
 