import { createStore } from 'vuex';

const store = createStore({
    state:{
    persons: [],
    votes: [],
    liste: [],
    },
    mutations: {
        ADD_PERSON(state, person){
            state.persons.push(person);
        },
        ADD_VOTE(state,vote){
            state.votes.push(vote);
        },
        berechne(state){
            const kandidaten= {};
            state.votes.forEach(vote=> {
                const{ vorname, nachname } = vote.person;
                if(!(vorname in kandidaten)) {
                    kandidaten[vorname] = { name: `${vorname} ${nachname}`, stimmen: 0};
                } kandidaten[vorname].stimmen += vote.weight;
        
                
            });
            const gesamtStimmen = state.vote.length;
            Object.values(kandidaten).forEach(Kandidat=> {
                Kandidat.prozent= ((Kandidat.stimmen / gesamtStimmen)* 100).toFixed(2);
            }
                );
                state.liste= Object.values(kandidaten).sort((a,b )=> b.stimmen - a.stimmen);
        }
    },


    actions:
{
    addPerson({ commit}, person) {
        commit('ADD_PERSON', person);
    }
},
getters:{
    kandidaten(state){
        return state.persons.filter(person => person.wählbar === 'wählbar');
    }
}
});
export default store;