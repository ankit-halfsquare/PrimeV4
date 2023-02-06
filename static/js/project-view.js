









var project_view_columns = [
  //{ template: "<input class='editBtn2' type='button' value='Act Upon'>", width: 100 },

  { id: "id", header: "Action", width: 100 ,template:(props)=>{
    //console.log("props",props);
    return `<input type='button' value='Act Upon' class='project_view_act_upon' id='${props.id}'>`;
  }},

  { id: "name", header: "Name", width: 200, },
  { id: "obsolete", header: "Obsolate Status", width: 100 },];


var projecct_view_data = [
  { id: 189, name: "Piping Trade To Do11", obsolate: "0", gender: "Male", active_user: 1 },
  { id: 190, name: "Piping Trade Done11", obsolate: "1", gender: "Male", active_user: 1 },
  { id: 191, name: "AT To Do11", obsolate: "0", gender: "Male", active_user: 1 },
  { id: 192, name: "QAR To Do", obsolate: "1", gender: "Female", active_user: 0 }
];



