function mark_status(value) {
    if (value === "Open") {
      return "highlight";
    }
    else if (value === "<span>Done</span>") {
      return "highlight2";
    }
  }

var project_cols=[
    /*{
        template: function(obj) {
        return "<input class='projectEditBtn' type='button' value='Act Upon' data-id='" + obj.id + "'>";
        },
        width:100
    },*/
    { id: "id", header: "Action", width: 100 ,template:(props)=>{
      //console.log("props",props);
      return `<input type='button' value='Act Upon' class='project_act_upon' id='${props.id}'>`;
    }},
    { id: "name", header: "Name", width: 125 },
    { id: "city", header: "City", width: 125 },
    { id: "state", header: "State", width: 100 },
    { id: "country", header: "Country", width: 100 },
    { id: "status", header: "Status", width: 100,cssFormat: mark_status },
    { id: "cost", header: "CostUnit", width: 125 },
    { id: "revenue", header: "Revenue", width: 125 },
    { id: "margin", header: "Margin", width: 125 },
    { id: "comments", header: "Comments", width: 125 }, 
    { id: "customer_feedback", header: "CustomerFeedback", width: 125 }, 

]