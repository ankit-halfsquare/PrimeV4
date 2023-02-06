var menu_data = [
  /*{
    id: "buildings", icon: "mdi mdi-view-dashboard", value: "Buildings(item sets)", data: [
      { id: "buildings1", value: "buildings 1" },
      { id: "buildings2", value: "buildings 2" }
    ]
  },*/
  {
    id: "project", icon: "mdi mdi-view-column", value: "Project(task set)", data: [
      { id: "project_select", value: "Project" },
      { id: "task", value: "Task" },
      /*{ id: "view_role_position_user", value: "View-Role-Position-User" },
      { id: "view_role_user", value: "View-Role-User" },
      { id: "project_position", value: "Project Position" },*/
    ]
  },
  /*{
    id: "tables", icon: "mdi mdi-table", value: "Dummy", data: [
      { id: "tables1", value: "Dummy" },
      { id: "tables2", value: "Dummy" },
      { id: "tables3", value: "Dummy" }
    ]
  },
  {
    id: "uis", icon: "mdi mdi-puzzle", value: "Dummy", data: [
      { id: "dataview", value: "Dummy" },
      { id: "list", value: "Dummy" },
      { id: "menu", value: "Dummy" },
      { id: "tree", value: "Dummy" }
    ]
  },
  {
    id: "tools", icon: "mdi mdi-calendar", value: "Dummy", data: [
      { id: "kanban", value: "Dummy" },
      { id: "pivot", value: "Dummy" },
      { id: "scheduler", value: "Dummy" }
    ]
  },
  {
    id: "forms", icon: "mdi mdi-pencil", value: "Dummy", data: [
      { id: "buttons", value: "Dummy" },
      { id: "selects", value: "Dummy" },
      { id: "inputs", value: "Dummy" }
    ]
  },
  { id: "demo", icon: "mdi mdi-book", value: "Dummy" }*/
];




var projects = []


var views_for_project = []



function mark_status_task_table(value) {
  if (value === "<span>Ready To Do (Backlog)</span>") {
    return "highlight";
  }
  else if (value === "<span>Done</span>") {
    return "highlight2";
  }else if (value === "<span>Not Ready To Do</span>") {
    return "highlight3";
  }
}





var task_columns= [
  

];

var task_columns1 = [
  { id: "task", header: { content: "excelFilter", text: "Task Summary" }, width: 150, },
  { id: "task_parent_name", header: { content: "excelFilter", text: "Parent Task" }, width: 100 },
  { id: "task", header: { content: "excelFilter", text: "Category" }, width: 100 },
  { id: "task", header: { content: "excelFilter", text: "Item" }, width: 100 },
  { id: "assignees", header: { content: "excelFilter", text: "Assignee" }, width: 100 },
  { id: "task_status", header: { content: "excelFilter", text: "Status" }, width: 150 },
  { id: "percent_complete", header: { content: "excelFilter", text: "Percent Complete" }, width: 100 },
  { id: "prerequisite_status", header: { content: "excelFilter", text: "Prerequisite status" }, width: 100 },
  { id: "additional_data_type_form_name", header: { content: "excelFilter", text: "Additional Data Form" }, width: 100 },
  { id: "task", header: { content: "excelFilter", text: "File Count" }, width: 100 },
  { id: "task_details", header: { content: "excelFilter", text: "Task Details" }, width: 150 },

];

var task_columns2 = [
  { id: "task", header: { content: "excelFilter", text: "Task Summary" }, width: 150, },
  { id: "task_parent_name", header: { content: "excelFilter", text: "Parent Task" }, width: 100 },
  { id: "task", header: { content: "excelFilter", text: "Category" }, width: 100 },
  { id: "task", header: { content: "excelFilter", text: "Item" }, width: 100 },
  { id: "assignees", header: { content: "excelFilter", text: "Assignee" }, width: 100 },
  { id: "task_status", header:{content: "excelFilter",text: "Status"}, width: 150},


 /* {
    id: "task_status", header: { text: "Status" }, width: 150,
    template: function (obj) {
      if (obj.task_status === 'done') {
        return "<span>Done</span>";
      }
      else if (obj.task_status === 'ready_to_do_backlog') {
        return "<span>Ready To Do (Backlog)</span>";
      }
      else {
        return obj.task_status;
      }
    },
    cssFormat: mark_status
  },*/


  { id: "percent_complete", header: { content: "excelFilter", text: "Percent Complete" }, width: 100 },
  { id: "prerequisite_status", header: { content: "excelFilter", text: "Prerequisite status" }, width: 100 },
  { id: "additional_data_type_form_name", header: { content: "excelFilter", text: "Additional Data Form" }, width: 100 },
  { id: "task", header: { content: "excelFilter", text: "File Count" }, width: 100 },
  { id: "task_details", header: { content: "excelFilter", text: "Task Details" }, width: 150 },

];