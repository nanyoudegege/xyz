# 实地解剖学 OCR 精校进度 / Field Anatomy OCR QC

这是一个**公开的质量控制与进度管理仓库**，用于跟踪《实地解剖学》第2版扫描PDF的逐页视觉核对、隐藏OCR文字层重建和回归验证。

> 版权边界：仓库不分发教材扫描件、完整OCR文本、逐页图片或校定PDF。这里只保存通用脚本、质量标准和不含教材正文的进度/审计元数据。

## 当前检查点

- 最新验证版本：**v169**
- 本轮：PDF **59-63** 页 / 书内 **36-40** 页
- 顺序精校进度：目录 PDF 6-23 页已重建；正文书内 **1-40页**已连续重建
- 本轮记录：**158条**；字符：**3,712个**（非空3,692个）
- 非空字符框零墨迹：**0**
- 全书低分辨率可见回归：**592/592页一致**
- 编辑页220 dpi双渲染器回归：PDFium **5/5**、Poppler **5/5**；与原扫描 **5/5一致**
- 书签：706项；批注：43页、282项；页码标签保留
- 下一批：PDF **64-68** 页 / 书内 **41-45** 页

## 进度文件

- [`progress/progress.csv`](progress/progress.csv)：逐版本检查点
- [`progress/page_status.csv`](progress/page_status.csv)：覆盖592页的分段状态
- [`progress/special_remediation.csv`](progress/special_remediation.csv)：早期高风险页定点修复记录
- [`docs/workflow.md`](docs/workflow.md)：精校与验证流程
- [`docs/audit-schema.md`](docs/audit-schema.md)：审计字段说明

## 验收口径

一页只有同时满足以下条件，才标记为 `complete_sequential_rebuild`：

1. 以原扫描图像逐行、逐图题、逐标签核对；
2. 旧OCR流被替换，字符按真实印刷位置重新建立坐标；
3. 内容流字符顺序和坐标可回读；
4. 非空字符框与原扫描墨迹相交；
5. 编辑页高分辨率可见像素不变；
6. 未编辑页、书签、页码标签、批注和页面几何不受影响。

## 仓库名称

当前使用此前空置的公开仓库 `nanyoudegege/xyz` 承载项目。建议后续在GitHub设置中将其重命名为 `field-anatomy-ocr-qc`；重命名不会改变仓库历史。
