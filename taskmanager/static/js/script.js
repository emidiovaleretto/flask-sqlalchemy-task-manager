document.addEventListener('DOMContentLoaded', function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
  });

  // modal initialization
  document.addEventListener('DOMContentLoaded', function() {
    let modal = document.querySelectorAll('.modal');
    M.Modal.init(modal);
  });

  // date picker initialization
  document.addEventListener('DOMContentLoaded', function() {
    let datePicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datePicker);
  });


  // select field initialization
  document.addEventListener('DOMContentLoaded', function() {
    let select = document.querySelectorAll('select');
    M.FormSelect.init(select);
  });