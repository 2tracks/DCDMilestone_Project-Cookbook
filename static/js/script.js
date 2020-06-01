
// Adds a new field to Ingredients on add_recipe.html

var new_ingredient = '<div id="new-ingredient"><div class="input-field col s11"><input placeholder="*Eq: 1/2 cup fresh orange juice" type="text" name="recipe_ingredients" class="validate" required></div><div class="col s1"><a class="btn-floating lime darken-4 waves-effect waves-light" id="del-ingredient"><i class="material-icons">delete_forever</i></a></div></div>';

$('#add-ingredient').click(function(){
    $('#ingredients').append(new_ingredient);
    Materialize.updateTextField();
});

$('body').on('click','#del-ingredient', function() {
    $(this).parents('#new-ingredient').remove();
});