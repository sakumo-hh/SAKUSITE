(function () {
    document.addEventListener('DOMContentLoaded', function() {
      const btn = document.getElementById('dropdown__btn');
      if(btn) {
        btn.addEventListener('click', function(){
          this.classList.toggle('is-open');
        });
      }
    });
  }());