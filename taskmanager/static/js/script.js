document.addEventListener('DOMContentLoaded', function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
  });

  // collapsible initialization
  let collapsible = document.querySelectorAll('.collapsible');
  M.Collapsible.init(collapsible);

  // modal initialization
  let modal = document.querySelectorAll('.modal');
  M.Modal.init(modal);


  // date picker initialization
  let datePicker = document.querySelectorAll('.datepicker');
  M.Datepicker.init(datePicker, {
    format: "dd mmmm, yyyy",
    i18n: {done: "Select"}
  });


  // select field initialization
  let select = document.querySelectorAll('select');
  M.FormSelect.init(select);
