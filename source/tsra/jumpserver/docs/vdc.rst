VDC项目环境搭建
==================
::

	#通过使用Jumpserver管理PC: 闲置、使用位置、防丢、盘点
	docker run --name jumpser156_vdc -d -v /home/jumpser156_vdc/media:/opt/jumpserver/data/media     -p 88:80     -p 2222:2222     -e SECRET_KEY=xxxxxxxxxxxxx     -e BOOTSTRAP_TOKEN=xxxxxx    -e DB_HOST=192.168.23.212     -e DB_PORT=3306     -e DB_USER=root     -e DB_PASSWORD='123456'     -e DB_NAME=vdc_track    jumpserver/jms_all:latest

1. 定制前端表格字段
----------------------
::

	对应表={
	    'Dept': '部门简称',  --- asset_vendor
	    'Dept_CN': '部级名称',  --- asset_memory
	    'UName': '用户名(UID)',  --- asset_hostname
	    'IP': 'IP地址',  --- asset_ip
	    'SN': 'SN',  --- asset_sn
	    'OS': 'WIN7/WIN10',  --- asset_os_arch
	    'CTime': '申请日期',  --- asset_date_created
	    'GPS': '使用位置',  --- asset_model
	    'UStatus': '用户状态或VM',  --- asset_cpu_model
	    'Type': '计费类型',  --- asset_os
	    'OLDays': '离线天数'  --- asset_cpu_cores 且必须cpu_count=0
	}

	users/templates/users/_granted_assets.html
	    <div class="mail-box-header">
	        {% include '_csv_import_export_mydev.html' %}    #apps/templates/_csv_import_export_mydev.html
	        <div class="btn-group" style="float: left">
	            <button class="btn btn-default btn-sm">{{ labels }}</button>
	        </div>
	        <table class="table table-striped table-bordered table-hover" id="user_assets_table" >
	            <thead>
	                <tr>
	                    <th class="text-center"><input type="checkbox" class="ipt_check_all"></th>
	                    <th class="text-center">{% trans 'Dept' %}</th>
	                    <th class="text-center">{% trans 'Dept_CN' %}</th>
	                    <th class="text-center">{% trans 'UName' %}</th>
	                    <th class="text-center">{% trans 'IP' %}</th>
	                    <th class="text-center">{% trans 'SN' %}</th>
	                    <th class="text-center">{% trans 'OS' %}</th>
	                    <th class="text-center">{% trans 'CTime' %}</th>
	                    <th class="text-center">{% trans 'GPS' %}</th>
	                    <th class="text-center">{% trans 'UStatus' %}</th>
	                    <th class="text-center">{% trans 'Type' %}</th>
	                    <th class="text-center">{% trans 'OLDays' %}</th>
	                </tr>
	            </thead>
	            <tbody>
	            </tbody>
	        </table>
	    </div>
	    
	function initTable() {
	    if (inited){
	        return assetTable
	    } else {
	        inited = true;
	    }
	    var options = {
	        ele: $('#user_assets_table'),
	        columnDefs: [
	            {targets: 1, createdCell: function (td, cellData, rowData) {
	             cellData = htmlEscape(cellData);
	             var assetDetailUrl = '{% url 'assets:asset-detail' pk=DEFAULT_PK %}'
	                 .replace("{{ DEFAULT_PK }}", rowData.id);
	             var detailBtn = '<a href="assetDetailUrl" class="asset-detail" data-asset="assetId">' + cellData + '</a>';
	             if (showAssetHref) {
	                 cellData = detailBtn.replace("assetDetailUrl", assetDetailUrl);
	             } else {
	                 detailBtn = detailBtn.replace("assetId", rowData.id);
	                 cellData = detailBtn.replace("assetDetailUrl", "");
	             }
	             $(td).html(cellData);
	            }},
	        ],
	        ajax_url: assetTableUrl,
	        columns: [
	            {data: "id"}, {data: "vendor" },{data: "memory" },{data: "hostname" }, {data: "ip" },
	            {data: "sn" },{data: "os_arch" },{data: "date_created" },{data: "model" },{data: "cpu_model" },{data: "os" },{data: "cpu_cores" },
	        ]
	    };
		
	    assetTable = jumpserver.initServerSideDataTable(options);
	    return assetTable
	}

2. 序列化前端字段
--------------------
::

	assets/templates/assets/user_asset_list.html
	    var assetTableUrl = "{% url 'api-perms:my-assets' %}?cache_policy=1";
	    $(document).ready(function () {
            assetTable = initTable();  #新增
            initCsvImportExport(assetTable, "{% trans "Asset" %}");  #新增, 否则无法导出CSV
	        ........
	    })
	
	perms\urls\asset_permission.py
	    path('assets/', api.UserGrantedAssetsApi.as_view(), name='my-assets')
	
	perms/serializers/user_permission.py
	    class AssetGrantedSerializer(serializers.ModelSerializer):
	        """
	        被授权资产的数据结构
	        """
	        protocols = ProtocolsField(label=_('Protocols'), required=False, read_only=True)
	        platform = serializers.ReadOnlyField(source='platform_base')
	        date_created = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)
	        
	        class Meta:
	            model = Asset
	            only_fields = [
	                "id", "hostname", "ip", "protocols", "os", 'domain',
	                "platform", "comment", "org_id","sn","cpu_cores","os_version","os_arch",
	                "created_by","model","vendor","cpu_model","date_created","memory"
	            ]
	            fields = only_fields + ['org_name']
	            read_only_fields = fields

3. 隐藏CSV的import及update
-----------------------------
::

	cp templates/_csv_import_export.html templates/_csv_import_export_mydev.html
	vi templates/_csv_import_export_mydev.html  #需要导出功能直接引用这个
	function initCsvImportExport(table, objectType, listUrl, hide) {
	    hide=["import","update"]  #新增这个
	    csvTable = table;
	    $(".csv_object_type").html(objectType);
	    csvListUrl = listUrl ? listUrl : csvTable.ajax.url();
	    if (hide && hide.length > 0) {
	        hide.forEach(function (v) {
	            $("#li_csv_" + v).hide();
	        })
	    }
	}
	vi users/templates/users/_granted_assets.html
	    <div class="mail-box-header">
	        {% include '_csv_import_export_mydev.html' %}
	        <table class="table table-striped table-bordered table-hover" id="user_assets_table" >

4. 添加时间显示
------------------
::

	users/templates/users/_granted_assets.html
	    <div class="mail-box-header">
	        {% include '_csv_import_export_mydev.html' %}
	        <div class="btn-group" style="float: left">
	            <button class="btn btn-default btn-sm">{{ labels }}</button>  #替换label标签
	        </div>
	        <table class="table table-striped table-bordered table-hover" id="user_assets_table" >

	assets/views/asset.py
	    class UserAssetListView(PermissionsMixin, TemplateView):
	        template_name = 'assets/user_asset_list.html'
	        permission_classes = [IsValidUser]
	     
	        def get_context_data(self, **kwargs):
	            context = {
	                'action': _('My assets'),
	                'labels': str(Asset.objects.values_list("id", flat=True).first())[:13].replace('-','')+'+4H',  #替换label标签内容
	                'show_actions': True
	                }
	        kwargs.update(context)
	        return super().get_context_data(**kwargs)

5. 允许普通认证用户导出CSV
-----------------------------
::

	common/urls/api_urls.py
	common/api.py
	    class ResourcesIDCacheApi(APIView):
	        #默认权限级别是apps/jumpserver/settings/libs.py的'DEFAULT_PERMISSION_CLASSES': ('common.permissions.IsOrgAdmin',)
	        #不建议降低libs.py的权限为IsValidUser
	        #views优先级别比默认的高
	        permission_classes = [IsValidUser]  #新增
	        def post(self, request, *args, **kwargs):
	            spm = str(uuid.uuid4())
	            resources_id = request.data.get('resources')
	            if resources_id:
	                cache_key = KEY_CACHE_RESOURCES_ID.format(spm)
	                cache.set(cache_key, resources_id, 300)
	            return Response({'spm': spm})

6. 操作历史
--------------
::

	[root@73655e16c433 apps]# history|grep html
	    100  vi users/templates/users/_granted_assets.html
	    110  vi users/templates/users/user_granted_asset.html
	    121  vi templates/_csv_import_export.html
	    130  vi users/templates/users/_user_detail_nav_header.html
	    136  vi assets/templates/assets/user_asset_list.html
	    160  vi templates/_nav_user.html
	    229  cp templates/_csv_import_export.html templates/_csv_import_export_mydev.html
	    230  vi templates/_csv_import_export_mydev.html
	    
	[root@73655e16c433 apps]# history|grep py
	    18  vi perms/serializers/user_permission.py
	    99  vi perms/serializers/user_permission.py
	    151  vi assets/views/asset.py
	    152  vi users/views/user.py
	    167  vi perms/api/user_permission/user_permission_assets.py
	    184  vi perms/api/mixin.py
	    206  vi common/api.py
	    224  vi jumpserver/settings/libs.py
	    250  vi assets/views/asset.py
	    252  vi assets/serializers/asset.py

7. 其他分析
--------------
::

	apps/templates/base.html
	apps/templates/_left_side_bar.html  #判断是否为普通用户还是管理员
	apps/templates/_nav_user.html  #普通用户, 根据权限定制侧边栏
	    {% url 'assets:user-asset-list' %}{% trans 'My assets' %}
	        assets/urls/views_urls.py
	            path('user-asset/', views.UserAssetListView.as_view(), name='user-asset-list'),
	                assets/views/asset.py
	                    class UserAssetListView(PermissionsMixin, TemplateView):
	                        template_name = 'assets/user_asset_list.html'
	                        permission_classes = [IsValidUser]
	                    assets/templates/assets/user_asset_list.html
	                        {% include 'users/_granted_assets.html' %}
	                            users/templates/users/_granted_assets.html  #最终显示的数据表格
	                                apps/statics/js/jumpserver.js  LN1083
	                                    function APIExportCSV(props) {
	                                        requestApi({
	                                            url: '/api/v1/common/resources/cache/',
	                                            data: JSON.stringify({resources: _objectsId}),
	                                            method: "POST",
	                                            flash_message: false,
	                                            success: function (data) {
	                                                exportUrl = setUrlParam(exportUrl, 'spm', data.spm);
	                                                console.log(exportUrl);  #/api/v1/perms/users/assets/?cache_policy=1&format=csv&spm=66b8cc13-00a8-423c-9dee-36ec02bafdd9
	                                                window.open(exportUrl);
	                                            },
	                                            failed: function () {
	                                                toastr.error(gettext('Export failed'));
	                                            }
	                                        });
	                                    }
	                                common/urls/api_urls.py
	                                common/api.py
	                                    class ResourcesIDCacheApi(APIView):
	                                        #默认权限级别是apps/jumpserver/settings/libs.py的'DEFAULT_PERMISSION_CLASSES': ('common.permissions.IsOrgAdmin',)
	                                        #不建议降低libs.py的权限为IsValidUser
	                                        #views优先级别比默认的高
	                                        permission_classes = [IsValidUser]  #新增
	                                        def post(self, request, *args, **kwargs):
	                                            spm = str(uuid.uuid4())
	                                            resources_id = request.data.get('resources')
	                                            if resources_id:
	                                                cache_key = KEY_CACHE_RESOURCES_ID.format(spm)
	                                                cache.set(cache_key, resources_id, 300)
	                                            return Response({'spm': spm})
	
	apps/templates/_nav.html  #管理员, 根据权限定制侧边栏
