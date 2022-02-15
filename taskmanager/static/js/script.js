document.addEventListener('DOMContentLoaded', function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
  });

  // collapsible initialization
  document.addEventListener('DOMContentLoaded', function() {
    let collapsible = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsible);
  });

  // modal initialization
  document.addEventListener('DOMContentLoaded', function() {
    let modal = document.querySelectorAll('.modal');
    M.Modal.init(modal);
  });

  // date picker initialization
  document.addEventListener('DOMContentLoaded', function() {
    let datePicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datePicker, {
      format: "dd mmm yyyy",
      i18n: {done: "Select"}
    });
  });

  // select field initialization
  document.addEventListener('DOMContentLoaded', function() {
    let select = document.querySelectorAll('select');
    M.FormSelect.init(select);
  });

  // dropdown initialization
  document.addEventListener('DOMContentLoaded', function() {
    let dropdown = document.querySelectorAll('.dropdown-trigger');
    M.Dropdown.init(dropdown);
  });