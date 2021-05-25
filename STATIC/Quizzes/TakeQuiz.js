$( document ).ready(function() {
    // Display first question
    $(".question-base:first-of-type").removeAttr('hidden');
    var correct = 0;

    $(".question-base input[type=radio]").on('change', function(){
        $(this).closest(".question-base").find('.CONFIRM').removeAttr('disabled');
    })

    // On Submit Click
    $(".CONFIRM").each(function(){
        $(this).click(function(){
            // Disable the submit button
            CONFIRM_BUTTON = $(this);
            this.disabled = true;
            // Disable the selection tools so no changes can happen to answers
            $(this).closest(".question-base").find("input[type=radio]").each(function(input,val){
                val.disabled = true;
            })
            // Find ID of selected radio
            ID = $(this).closest(".question-base").find("input[type=radio]:checked").data("choiceid");
            // Submit request to check answer
            $.ajax({
                url: `/fetch/${ID}`
            }).done(function(data){
                if(data.Value){
                    correct++;
                    $("#polls").append(`
                    <div class="card bg-success" data-aos="fade-up">
                        <h5 class="card-header"><i class="fas fa-check"></i> Correct</h5>
                        <div class="card-body">
                            <p class="card-text">${data.Percentage}% of other quiz takers also chose your answer.</p>
                        </div>
                    </div>
                    `)
                }
                else{
                    $("#polls").append(`
                    <div class="card bg-danger" data-aos="fade-up">
                        <h5 class="card-header"><i class="fas fa-times"></i> Incorrect</h5>
                        <div class="card-body">
                            <p class="card-text">${data.Percentage}% of other quiz takers also chose your answer.</p>
                        </div>
                    </div>
                    `)
                }
                // Now display the reasoning and then enable the next button.
                $("#reasoning").append(`
                <div class="card bg-info" data-aos="fade-up">
                    <h5 class="card-header"><i class="fas fa-info-circle"></i> Explanation</h5>
                    <div class="card-body">
                        <p class="card-text">${data.Reasoning}</p>
                    </div>
			    </div>
                `);
                CONFIRM_BUTTON.closest(".question-base").find('.NEXT').removeAttr('disabled');
            })
        })
    })
    // Logic for when the next button is clicked
    $(".NEXT").each(function(){
        $(this).click(function(){
            $(this).disable = true;
            // Remove cards from reasoning and results
            $("#polls").first().fadeOut(400,function(){
                $(this).find(".card").remove();
                $(this).show();
            })
            $("#reasoning").first().fadeOut(400,function(){
                $(this).find(".card").remove();
                $(this).show();
            })
            // Update correct
            $("#output").text(correct);
            // Remove previous question and replace with new one.
            $(this).closest(".question-base").fadeOut(400, function(){
                // What to do after the question is faded out.
                $(this).remove();
                $(".question-base:first-of-type").removeAttr('hidden');
            })
        })
    })
});