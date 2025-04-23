// Open modals
document.querySelectorAll('[data-toggle="modal"]').forEach(button => {
    button.addEventListener('click', function () {
      const target = document.querySelector(this.dataset.target);
      if (target) {
        target.classList.add('show');
      }
    });
  });
  
  // Close modals
  document.querySelectorAll('.modal .close, .modal .btn[data-dismiss="modal"]').forEach(button => {
    button.addEventListener('click', function () {
      const modal = this.closest('.modal');
      if (modal) {
        modal.classList.remove('show');
      }
    });
  });
  
  // Close on backdrop click
  document.querySelectorAll('.modal').forEach(modal => {
    modal.addEventListener('click', function (e) {
      if (e.target === modal) {
        modal.classList.remove('show');
      }
    });
  });
  