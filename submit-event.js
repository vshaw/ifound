(function() {
  var form = document.getElementById('contact)');

  addEvent(form, 'submit', function(e) {
    e.preventDefault();
    var elements = this.elements;
    var msg = 'Your contact inforation has been succesfully updated!';
    document.getElementById('main')/textCpmtemt = msg;
  });
}());
