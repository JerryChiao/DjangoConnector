/**
 * Created by zhaoyin on 2017/12/20.
 */
        function goto_modify_pcb(obj){
            var row = obj.parentNode.parentNode;
            var td = $(row).find("td");
            var witc = td.eq(0).text();
            var data = {witc: witc};
            $.ajaxSetup({
                data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
            });

            $.ajax({
                type:"POST",
                url: "{% url 'admin_load_connector_pcb_form' %}",
                data: data,
                cache:false,
                success: function(data) {
                    if(data == -1 ){
                        alert("该记录已经存在");
                    }
                    document.getElementById("modify_pcb_witc").innerHTML=witc
                    $('#replace_part_pcb').html(data);
                    $("#modify_connector_pcb").modal("show");

                },
                error: function() {
                    $('.loginError').html('请求失败，请刷新页面后重试').show();
                }
            });
            return false;

        }

        function goto_delete_pcb(obj){
            var row = obj.parentNode.parentNode;
            var td = $(row).find("td");
            var witc = td.eq(0).text();
            document.getElementById("delete_pcb_witc").innerHTML=witc;
            $("#delete_pcb_modal").modal("show");
        }

        function do_delete_pcb(){
            var witc = document.getElementById("delete_pcb_witc").innerHTML;
            var dataForm = new FormData();
            dataForm.append("witc", witc);
            $.ajaxSetup({
                data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
            });

            $.ajax({
                type:"POST",
                url: "{% url 'admin_delete_pcb_connector' %}",
                data: dataForm,
                contentType: false,
                processData: false,
                success: function(data) {
                    if(data == -1 ){
                        alert("该记录已经存在");
                        return;
                    }
                    $("#delete_pcb_modal").modal("hide");
                    filter_connector_pcb_with_page();
                },
                error: function() {
                    $('.loginError').html('请求失败，请刷新页面后重试').show();
                }
            });
            return false;
        }

        function filter_connector_pcb_with_page(page){
            var formData = new FormData(document.getElementById("connector_pcb_form_filter"));

            if(typeof(page) != 'undefined'){
                formData.append('page', page)
            }

            $.ajaxSetup({
                data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
            });

            $.ajax({
                type:"POST",
                url: "{% url 'admin_filter_connector_pcb' %}",
                data: formData,
                cache:false,
                contentType: false,
                processData: false,
                success: function(data) {
                    if(data == -1 ){
                        alert("该记录已经存在");
                        return;
                    }
                    $('#filter_pcb_results').html(data);
                },
                error: function() {
                    $('.loginError').html('请求失败，请刷新页面后重试').show();
                }
            });
            return false;
        }

        $('#connector_pcb_form').submit(function(){
            var formData = new FormData(document.getElementById("connector_pcb_form"));
            $.ajaxSetup({
                data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
            });

            $.ajax({
                type:"POST",
                url: "{% url 'admin_add_pcb_connector' %}",
                data: formData,
                cache:false,
                contentType: false,
                processData: false,
                success: function(data) {
                    if(data == -1 ){
                        alert("该记录已经存在");
                    }
                    $('#connector_pcb_form_reset').trigger("click");
                    $('#result_display').html(data);
                },
                error: function() {
                    $('.loginError').html('请求失败，请刷新页面后重试').show();
                }
            });
            return false;
        });

        $('#modify_connector_pcb_form').submit(function(){
            var formData = new FormData(document.getElementById("modify_connector_pcb_form"));
            var raw_witc = document.getElementById("modify_pcb_witc").innerHTML;
            formData.append('raw_witc', raw_witc);
            $.ajaxSetup({
                data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
            });

            $.ajax({
                type:"POST",
                url: "{% url 'admin_modify_connector_pcb' %}",
                data: formData,
                cache:false,
                contentType: false,
                processData: false,
                success: function(data) {
                    if(data == -1 ){
                        alert("该记录已经存在");
                        return;
                    }
                    $("#modify_connector_pcb").modal("hide");
                    filter_connector_pcb_with_page();
                },
                error: function() {
                    $('.loginError').html('请求失败，请刷新页面后重试').show();
                }
            });
            return false;
        });

        $('#connector_pcb_form_filter').submit(filter_connector_pcb_with_page);

        function filter_connector_cable_with_page(page){

            var formData = new FormData(document.getElementById("connector_cable_form_filter"));

            if (typeof(page) == 'undefined'){

            }else{
                formData.append('page', page);
            }

            $.ajaxSetup({
                data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
            });

            $.ajax({
                type:"POST",
                url: "{% url 'admin_filter_connector_cable' %}",
                data: formData,
                cache:false,
                contentType: false,
                processData: false,
                success: function(data) {
                    if(data == -1 ){
                        alert("该记录已经存在");
                        return;
                    }
                    $('#connector_cable_filter_results').html(data);
                },
                error: function() {
                    $('.loginError').html('请求失败，请刷新页面后重试').show();
                }
            });
            return false;
        };


        function goto_modify_cable(obj){
            var row = obj.parentNode.parentNode;
            var td = $(row).find("td");
            var witc = td.eq(0).text();
            var data = {witc: witc};
            $.ajaxSetup({
                data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
            });

            $.ajax({
                type:"POST",
                url: "{% url 'admin_load_connector_cable_form' %}",
                data: data,
                cache:false,
                success: function(data) {
                    if(data == -1 ){
                        alert("该记录已经存在");
                        return;
                    }
                    document.getElementById("modify_cable_witc").innerHTML=witc
                    $('#replace_part_cable').html(data);
                    $("#modify_connector_cable").modal("show");

                },
                error: function() {
                    $('.loginError').html('请求失败，请刷新页面后重试').show();
                }
            });
            return false;

        }

        function goto_delete_cable(obj){
            var row = obj.parentNode.parentNode;
            var td = $(row).find("td");
            var witc = td.eq(0).text();
            document.getElementById("delete_cable_witc").innerHTML=witc;
            $("#delete_cable_modal").modal("show");
        }

        function do_delete_cable(){
            var witc = document.getElementById("delete_cable_witc").innerHTML;
            var dataForm = new FormData();
            dataForm.append("witc", witc);
            $.ajaxSetup({
                data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
            });

            $.ajax({
                type:"POST",
                url: "{% url 'admin_delete_cable_connector' %}",
                data: dataForm,
                contentType: false,
                processData: false,
                success: function(data) {
                    if(data == -1 ){
                        alert("该记录已经存在");
                        return;
                    }
                    $("#delete_cable_modal").modal("hide");
                    filter_connector_cable_with_page();
                },
                error: function() {
                    $('.loginError').html('请求失败，请刷新页面后重试').show();
                }
            });
            return false;
        }

        $('#connector_cable_form').submit(function(){
            var formData = new FormData(document.getElementById("connector_cable_form"));
            $.ajaxSetup({
                data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
            });

            $.ajax({
                type:"POST",
                url: "{% url 'admin_add_cable_connector' %}",
                data: formData,
                cache:false,
                contentType: false,
                processData: false,
                success: function(data) {
                    if(data == -1 ){
                        alert("该记录已经存在");
                    }

                    $('#result_display').html(data);
                    $('#connector_cable_form_reset').trigger("click");
                },
                error: function() {
                    $('.loginError').html('请求失败，请刷新页面后重试').show();
                }
            });
            return false;
        });

        $('#modify_connector_cable_form').submit(function(){
            var formData = new FormData(document.getElementById("modify_connector_cable_form"));
            var raw_witc = document.getElementById("modify_cable_witc").innerHTML;
            formData.append('raw_witc', raw_witc);
            $.ajaxSetup({
                data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
            });

            $.ajax({
                type:"POST",
                url: "{% url 'admin_modify_connector_cable' %}",
                data: formData,
                cache:false,
                contentType: false,
                processData: false,
                success: function(data) {
                    if(data == -1 ){
                        alert("该记录已经存在");
                        return;
                    }
                    $("#modify_connector_cable").modal("hide");
                    filter_connector_cable_with_page();
                },
                error: function() {
                    $('.loginError').html('请求失败，请刷新页面后重试').show();
                }
            });
            return false;
        });

        $('#connector_cable_form_filter').submit(filter_connector_cable_with_page)