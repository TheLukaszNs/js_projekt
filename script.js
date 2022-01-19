const items = document.querySelectorAll('.data-item');
document.addEventListener('DOMContentLoaded', () => {
  items.forEach(item => {
    item.addEventListener('click', () => {
      item.classList.toggle('active');
    });
  });
});