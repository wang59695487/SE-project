<?php if (!defined('THINK_PATH')) exit();?><!DOCTYPE html>

<!--[if IE 8]> <html lang="en" class="ie8"> <![endif]-->

<!--[if IE 9]> <html lang="en" class="ie9"> <![endif]-->

<!--[if !IE]><!--> <html lang="en"> <!--<![endif]-->

<!-- BEGIN HEAD -->

<head>

	<meta charset="utf-8" />

	<title>股票交易管理系统</title>

	<meta content="width=device-width, initial-scale=1.0" name="viewport" />

	<meta content="" name="description" />

	<meta content="" name="author" />

	<!-- BEGIN GLOBAL MANDATORY STYLES -->

	<link href="__PUBLIC__/tms/media/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>

	<link href="__PUBLIC__/tms/media/css/bootstrap-responsive.min.css" rel="stylesheet" type="text/css"/>

	<link href="__PUBLIC__/tms/media/css/font-awesome.min.css" rel="stylesheet" type="text/css"/>

	<link href="__PUBLIC__/tms/media/css/style-metro.css" rel="stylesheet" type="text/css"/>

	<link href="__PUBLIC__/tms/media/css/style.css" rel="stylesheet" type="text/css"/>

	<link href="__PUBLIC__/tms/media/css/style-responsive.css" rel="stylesheet" type="text/css"/>

	<link href="__PUBLIC__/tms/media/css/default.css" rel="stylesheet" type="text/css" id="style_color"/>

	<link href="__PUBLIC__/tms/media/css/uniform.default.css" rel="stylesheet" type="text/css"/>

	<!-- END GLOBAL MANDATORY STYLES -->

	<!-- BEGIN PAGE LEVEL STYLES -->

	<link rel="stylesheet" type="text/css" href="__PUBLIC__/tms/media/css/select2_metro.css" />

	<link rel="stylesheet" href="__PUBLIC__/tms/media/css/DT_bootstrap.css" />

	<!-- END PAGE LEVEL STYLES -->

	<link rel="shortcut icon" href="__PUBLIC__/tms/media/image/favicon.ico" />
<script type="text/javascript">
function pt_user_manage_choose(button_name){
	if(button_name=="delete_user"){
		document.pt_user_manage.action="<?php echo U('Root/deletePuTongUser');?>";
		
	}
	else if(button_name=="lock_user"){
	   document.pt_user_manage.action="<?php echo U('Root/lockPuTongUser');?>";
	}
	
	else if(button_name=="resetpassword_user"){
	  document.pt_user_manage.action="<?php echo U('Root/resetpasswordPuTongUser');?>";
	}
	else{
		document.pt_user_manage.action="<?php echo U('Root/putongUserManageIndex');?>";
	}
}
</script>
</head>

<!-- END HEAD -->

<!-- BEGIN BODY -->

<!-- <body class="page-header-fixed"> -->
<body class="page-header-fixed page-sidebar-fixed page-sidebar-closed">
	<!-- BEGIN HEADER -->

	<div class="header navbar navbar-inverse navbar-fixed-top">

		<!-- BEGIN TOP NAVIGATION BAR -->

		<div class="navbar-inner">

			<div class="container-fluid">

				<!-- BEGIN LOGO -->

				<a class="brand" href="index.html">

				<!-- <img src="__PUBLIC__/tms/media/image/logo.png" alt="logo" /> -->
				<p> 股票交易管理系统</p>

				</a>

				<!-- END LOGO -->

				<!-- BEGIN RESPONSIVE MENU TOGGLER -->

				<a href="javascript:;" class="btn-navbar collapsed" data-toggle="collapse" data-target=".nav-collapse">

				<img src="__PUBLIC__/tms/media/image/menu-toggler.png" alt="" />

				</a>

				<!-- END RESPONSIVE MENU TOGGLER -->

				<!-- BEGIN TOP NAVIGATION MENU -->

				<ul class="nav pull-right">

					<!-- BEGIN USER LOGIN DROPDOWN -->

					<li><a href="<?php echo U('Index/logout');?>"><i class="icon-key"></i>退出</a></li>


					<!-- END USER LOGIN DROPDOWN -->

				</ul>

				<!-- END TOP NAVIGATION MENU -->

			</div>

		</div>

		<!-- END TOP NAVIGATION BAR -->

	</div>

	<!-- END HEADER -->

	<!-- BEGIN CONTAINER -->

	<div class="page-container row-fluid">

		<!-- BEGIN SIDEBAR -->

		<!-- BEGIN SIDEBAR -->

		<div class="page-sidebar nav-collapse collapse">

			<!-- BEGIN SIDEBAR MENU -->

			<ul class="page-sidebar-menu">

				<li>

					<!-- BEGIN SIDEBAR TOGGLER BUTTON -->

					<div class="sidebar-toggler hidden-phone"></div>

					<!-- BEGIN SIDEBAR TOGGLER BUTTON -->

				</li>

				<li>
				</li>

				<!-- <li class="start "> -->
				<li class="">
					<a href="<?php echo U('Root/rootUserIndex');?>">

					<i class="icon-th"></i>

					<span class="title">添加新管理员</span>

					</a>

				</li>
				<li class="active">
					<a href="<?php echo U('Root/putongUserManageIndex');?>">

					<i class="icon-th"></i>

					<span class="title">管理业务管理员</span>

					</a>

				</li>
				<li class="">
					<a href="<?php echo U('Root/putongUserAuthIndex');?>">

					<i class="icon-th"></i>

					<span class="title">设置业务管理员权限</span>

					</a>

				</li>



				<!-- <li class="active ">

					<a href="javascript:;">

					<i class="icon-table"></i>

					<span class="title">Form Stuff</span>

					<span class="selected"></span>

					<span class="arrow open"></span>

					</a>

					<ul class="sub-menu">





						<li class="active">

							<a href="form_wizard.html">

							添加新管理员</a>

						</li>





					</ul>

				</li>
 -->

			</ul>

			<!-- END SIDEBAR MENU -->

		</div>

		<!-- END SIDEBAR -->

		<!-- BEGIN PAGE -->

		<div class="page-content">

			<!-- BEGIN SAMPLE PORTLET CONFIGURATION MODAL FORM-->

			<div id="portlet-config" class="modal hide">

				<div class="modal-header">

					<button data-dismiss="modal" class="close" type="button"></button>

					<h3>portlet Settings</h3>

				</div>

				<div class="modal-body">

					<p>Here will be a configuration form</p>

				</div>

			</div>

			<!-- END SAMPLE PORTLET CONFIGURATION MODAL FORM-->

			<!-- BEGIN PAGE CONTAINER-->

			<div class="container-fluid">

				<!-- BEGIN PAGE HEADER-->

				<div class="row-fluid">

					<div class="span12">

						<!-- BEGIN STYLE CUSTOMIZER -->



						<!-- END BEGIN STYLE CUSTOMIZER -->

						<!-- BEGIN PAGE TITLE & BREADCRUMB-->

						<h3 class="page-title">

							管理业务管理员 <small></small>

						</h3>

						<!-- END PAGE TITLE & BREADCRUMB-->

					</div>

				</div>

				<!-- END PAGE HEADER-->

				<!-- BEGIN PAGE CONTENT-->

				<div class="row-fluid">

					<div class="span12">

						<!-- BEGIN EXAMPLE TABLE PORTLET-->

						<div class="portlet box light-grey">

							<div class="portlet-title">

								<div class="caption"><i class="icon-globe"></i></div>

								<div class="tools">

									<a href="javascript:;" class="collapse"></a>

		

									<a href="javascript:;" class="remove"></a>

								</div>

							</div>
                            <div class="portlet-body">
							<form name="pt_user_manage" method="post" >
							

								<div class="clearfix">

									<div class="btn-group">

										<!-- <button id="sample_editable_1_new" class="btn green">

										Add New <i class="icon-plus"></i>

										</button> -->

									</div>

									<div class="btn-group pull-right">

										<button style="color:#000; font-weight: bold;" class="btn dropdown-toggle" data-toggle="dropdown">操作 <i class="icon-angle-down"></i>

										</button>

										<ul class="dropdown-menu pull-right">
                                        

											<li> <button   style="color:#000; font-weight: bold;" class="btn blue dropdown-toggle" type="submit" name="delete_user" onclick="pt_user_manage_choose(this.name)">删除</button></li>

											<li>  <button  style="color:#000; font-weight: bold;" class="btn blue dropdown-toggle" type="submit" name="refresh_user" onclick="pt_user_manage_choose(this.name)">刷新</button></li>

											<li> <button  style="color:#000; font-weight: bold;" class="btn blue dropdown-toggle" type="submit" name="lock_user" onclick="pt_user_manage_choose(this.name)">锁定/解锁</button></li>
											<li><button  style="color:#000; font-weight: bold;" class="btn blue dropdown-toggle" type="submit" name="resetpassword_user" onclick="pt_user_manage_choose(this.name)">密码重置</button></li>
										</ul>

									</div>

								</div>

								<table class="table table-striped table-bordered table-hover" id="sample_1">

									<thead>

										<tr>

											<th style="width:8px;"><input type="hidden" class="group-checkable" /></th>
											<th style="text-align:center;">管理员ID</th>
											<th style="text-align:center;">管理员账号</th>

											<!--  <th class="hidden-480">管理股票数量</th>  -->

										

											<th style="text-align:center;" class="hidden-480">管理员状态</th>

											<!-- <th ></th> -->

										</tr>

									</thead>
									
									<tbody>
									<?php if(is_array($list)): $i = 0; $__LIST__ = $list;if( count($__LIST__)==0 ) : echo "" ;else: foreach($__LIST__ as $key=>$vo): $mod = ($i % 2 );++$i;?><tr class="odd gradeX">

											<td style="text-align:center;"><label><input type="radio" name="PtUserRadioGroup" value="<?php echo ($vo["uid"]); ?>" id="PtUserRadioGroup.<?php echo ($key); ?>"></label></td>

											<td style="text-align:center;"><input  type="hidden"><?php echo ($vo["uid"]); ?> </input></td>
											<td style="text-align:center;"><input  type="hidden"><?php echo ($vo["userName"]); ?> </input></td>

											<!--   <td class="hidden-480">120</td>  -->

											

											<td ><span class="<?php if(($vo["active_status"]) == "1"): ?>label label-success<?php else: ?>label label-warning<?php endif; ?>"><?php if(($vo["active_status"]) == "1"): ?>正常<?php else: ?>锁定<?php endif; ?></span></td>  <!--  双引号内加thinkphp标签可以将返回值以字符串付给class 属性-->

											</tr><?php endforeach; endif; else: echo "" ;endif; ?>
									</tbody>
									
								</table>

							
						</form>
                        </div>
						</div>

						<!-- END EXAMPLE TABLE PORTLET-->

					</div>

				</div>



				<!-- END PAGE CONTENT-->

			</div>

			<!-- END PAGE CONTAINER-->

		</div>

		<!-- END PAGE -->

	</div>

	<!-- END CONTAINER -->

	<!-- BEGIN FOOTER -->

	<div class="footer">

		<div class="footer-inner">

			2014 &copy; a6

		</div>

		<div class="footer-tools">

			<span class="go-top">

			<i class="icon-angle-up"></i>

			</span>

		</div>

	</div>

	<!-- END FOOTER -->

	<!-- BEGIN JAVASCRIPTS(Load javascripts at bottom, this will reduce page load time) -->

	<!-- BEGIN CORE PLUGINS -->

	<script src="__PUBLIC__/tms/media/js/jquery-1.10.1.min.js" type="text/javascript"></script>

	<script src="__PUBLIC__/tms/media/js/jquery-migrate-1.2.1.min.js" type="text/javascript"></script>

	<!-- IMPORTANT! Load jquery-ui-1.10.1.custom.min.js before bootstrap.min.js to fix bootstrap tooltip conflict with jquery ui tooltip -->

	<script src="__PUBLIC__/tms/media/js/jquery-ui-1.10.1.custom.min.js" type="text/javascript"></script>

	<script src="__PUBLIC__/tms/media/js/bootstrap.min.js" type="text/javascript"></script>

	<!--[if lt IE 9]>

	<script src="__PUBLIC__/tms/media/js/excanvas.min.js"></script>

	<script src="__PUBLIC__/tms/media/js/respond.min.js"></script>

	<![endif]-->

	<script src="__PUBLIC__/tms/media/js/jquery.slimscroll.min.js" type="text/javascript"></script>

	<script src="__PUBLIC__/tms/media/js/jquery.blockui.min.js" type="text/javascript"></script>

	<script src="__PUBLIC__/tms/media/js/jquery.cookie.min.js" type="text/javascript"></script>

	<script src="__PUBLIC__/tms/media/js/jquery.uniform.min.js" type="text/javascript" ></script>

	<!-- END CORE PLUGINS -->

	<!-- BEGIN PAGE LEVEL PLUGINS -->

	<script type="text/javascript" src="__PUBLIC__/tms/media/js/select2.min.js"></script>

	<script type="text/javascript" src="__PUBLIC__/tms/media/js/jquery.dataTables.js"></script>

	<script type="text/javascript" src="__PUBLIC__/tms/media/js/DT_bootstrap.js"></script>

	<!-- END PAGE LEVEL PLUGINS -->

	<!-- BEGIN PAGE LEVEL SCRIPTS -->

	<script src="__PUBLIC__/tms/media/js/app.js"></script>

	<script src="__PUBLIC__/tms/media/js/table-managed.js"></script>

	<script>

		jQuery(document).ready(function() {

		   App.init();

		   TableManaged.init();

		});

	</script>

<script type="text/javascript">  var _gaq = _gaq || [];  _gaq.push(['_setAccount', 'UA-37564768-1']);  _gaq.push(['_setDomainName', 'keenthemes.com']);  _gaq.push(['_setAllowLinker', true]);  _gaq.push(['_trackPageview']);  (function() {    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;    ga.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'stats.g.doubleclick.net/dc.js';    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);  })();</script></body>

<!-- END BODY -->

</html>