webix.ui({
    view: "sidemenu",
    id: "menu2",
    width: 1500,
    position: "right",
    state:function(state){
      state.bottom = $$("menu").$height;
    },
    css: "my_menu2",
    body:{
      borderless:true,
      margin: 5,
      rows:[
      {
        id: "main",
        template: "will do something here",
        height:50
      },
      {
        id: "mydatatable2",
        view: "datatable",
        
        columns: project_view_columns,
        data: projecct_view_data,
        width: 1500,
        select: "row",
        editable: true,
        
        on: {
          
          onAfterEditStop: function(state, editor, ignoreUpdate) {



            if (!ignoreUpdate) {
              var row = this.getItem(editor.row);
              var checkboxValue = row.active_user ? "Yes" : "No";
              // rest of the code for saving data to the database
              console.log("checkboxValue",checkboxValue)
            }
           
            console.log("editor",editor.column)
            console.log("editor",editor.row)
            console.log("state.value",state.value)
            console.log("state.old",state.old)
          if (state.value != state.old) {
          // Perform an AJAX call to save the changes to the database
          //webix.ajax().put("/update_data", { id: state.id, column: state.column, value: state.value });
          }
          }
          },
          onAfterEditStop: function(state) {
            console.log("other function ",state)
            if (state.value != state.old) {
                // update the database with the new value of the checkbox
                // code to save data to database
            }
        },

        onClick:{
          "editBtn2":function(ev){
            console.log("----")
          }
        } ,
        onAfterEditStop: function(state) {
          console.log("other function ",state)
          if (state.value != state.old) {
              // update the database with the new value of the checkbox
              // code to save data to database
          }
      },
        
        
         
      },
      
      ]
    }
  });