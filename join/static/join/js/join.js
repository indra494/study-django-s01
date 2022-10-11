let join = (function () {
  return {
    goDetail: function (url) {
      location.href = url;
    },

    addHobbyForm: function(form) {
      let parent = form.parentNode.parentNode.parentNode;
      let element = form.parentNode.parentNode.cloneNode(true);      
      element.querySelector("[name='hobby_text']").value = "";

      let removeElement = parent.querySelector("[name='btn_add_hobby']");
      removeElement.parentNode.removeChild(removeElement);
          
      parent.append(element);
    },
    
    delHobbyForm:function(form) {
      let removeNode = form.parentNode.parentNode;
      removeNode.parentNode.removeChild(removeNode);
    }

  };
})();
