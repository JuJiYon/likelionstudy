const me = {
    name : "주지윤",
    age : 22,
    gender : 'female'
};
const someone = {
    name : "dd",
    age : 28,
    gender : "male",
};

function addMilitaryStateIfMale(person) {
    if (person.gender ==='female' ){
        person.addMilitaryState = false;
    }
}
    addMilitaryStateIfMale(me);
    addMilitaryStateIfMale(someone);

    console.log(me);
    console.log(someone);

    function parseBoolean(value){
        if (value === true){
            return "참";
        } else if (value === false){
            return "거짓";
        }
        }
    if (me.addMilitaryState !== undefined){
        console.log(parseBoolean(me.addMilitaryState));
    }
    if (someone.addMilitaryState !== undefined){
        console.log(parseBoolean(me.addMilitaryState));
    }
    