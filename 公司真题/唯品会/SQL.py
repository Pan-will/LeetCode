"""
DROP TABLE IF EXISTS `sales`;
CREATE TABLE `sales` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sku_no` int(11) NOT NULL COMMENT '商品编号',
  `qty` int(11) NOT NULL COMMENT '销量',
  `order_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '订单日期',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `sales`
-- ----------------------------
BEGIN;
INSERT INTO `sales` VALUES ('1', '1', '3', '2021-08-25 21:42:38'), ('2', '2', '2', '2021-08-25 21:42:43'), ('3', '3', '2', '2021-08-25 21:42:49'), ('4', '3', '2', '2021-08-25 21:42:52');
COMMIT;

-- ----------------------------
--  Table structure for `sku_info`
-- ----------------------------
DROP TABLE IF EXISTS `sku_info`;
CREATE TABLE `sku_info` (
  `sku_no` int(11) NOT NULL COMMENT '商品编号',
  `sku_name` varchar(20) NOT NULL COMMENT '商品名',
  `category` varchar(10) NOT NULL COMMENT '品类',
  PRIMARY KEY (`sku_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `sku_info`
-- ----------------------------
BEGIN;
INSERT INTO `sku_info` VALUES ('1', 'sku1', 'cat1'), ('2', 'sku2', 'cat2'), ('3', 'sku3', 'cat1');
COMMIT;
"""

"""
select a.sku_name, a.category, max(b.qty) from sku_info a
join sales b on a.sku_no=b.sku_no
group by a.category;
"""
