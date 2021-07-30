"""Exceptions auto-generated from error codes in St7API.py by _exceptions_generate.py"""


class St7BaseException(BaseException):
    """Base class for all ERR7_ and SE_ errors"""

    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def __str__(self):
        return f"{self.__class__.__name__}: {self.__doc__}"


class St7UnknownException(St7BaseException):
    """Unknown St7 Error"""

    pass


class ERR7_APIAlreadyInitialised(St7BaseException):
    """The API is already initialised."""

    pass


class ERR7_APIModuleNotLicensed(St7BaseException):
    """The API is not licensed or is incorrectly configured."""

    pass


class ERR7_APINotInitialised(St7BaseException):
    """The API is not initialised - St7Init has not been called."""

    pass


class ERR7_AnimationDimensionsTooLarge(St7BaseException):
    """Animation dimension is too large."""

    pass


class ERR7_AnimationDimensionsTooSmall(St7BaseException):
    """Animation dimension is too small."""

    pass


class ERR7_AnimationHandleOutOfRange(St7BaseException):
    """The specified animation handle is outside the valid range."""

    pass


class ERR7_AnimationNotRunning(St7BaseException):
    """The requested animation is not running."""

    pass


class ERR7_AutoMesherModuleNotLicensed(St7BaseException):
    """The AutoMesher Module is not licensed."""

    pass


class ERR7_BeamIsNotBXS(St7BaseException):
    """The specified beam property is not a BXS beam."""

    pass


class ERR7_CannotCalculateBXSData(St7BaseException):
    """The beam section data cannot be calculated."""

    pass


class ERR7_CannotCombResFiles(St7BaseException):
    """The result files cannot be combined."""

    pass


class ERR7_CannotCommunicate(St7BaseException):
    """
    The API is running in NETWORK mode but cannot communicate with the NetHASP licence manager.
    """

    pass


class ERR7_CannotEditSolverFiles(St7BaseException):
    """Result files generated directly by the solver cannot be edited."""

    pass


class ERR7_CannotFindNetworkLock(St7BaseException):
    """The API is running in NETWORK mode but has lost contact with the NETWORK hardware lock."""

    pass


class ERR7_CannotFindStandaloneLock(St7BaseException):
    """The API is running in STANDALONE mode but cannot find the STANDALONE hardware lock."""

    pass


class ERR7_CannotInitialiseDirectX(St7BaseException):
    """Cannot initialise Direct X - all graphics functionality will be disabled."""

    pass


class ERR7_CannotMakeBXS(St7BaseException):
    """The beam section cannot be generated."""

    pass


class ERR7_CannotMorphEdges(St7BaseException):
    """A morphed edge cannot be created due to fixed vertex constraints."""

    pass


class ERR7_CannotOpenResultFile(St7BaseException):
    """The result file cannot be opened."""

    pass


class ERR7_CannotReadBXS(St7BaseException):
    """The BXS data cannot be read."""

    pass


class ERR7_CannotReadFile(St7BaseException):
    """Cannot read from file."""

    pass


class ERR7_CannotReadImportFile(St7BaseException):
    """The import file cannot be read."""

    pass


class ERR7_CannotSaveFile(St7BaseException):
    """Cannot save file."""

    pass


class ERR7_CannotSaveImageFile(St7BaseException):
    """Cannot save image file."""

    pass


class ERR7_CannotSaveIniFile(St7BaseException):
    """Cannot save INI file."""

    pass


class ERR7_CannotSetWindowParent(St7BaseException):
    """Cannot set the specified model window parent."""

    pass


class ERR7_CannotWriteExportFile(St7BaseException):
    """The export file cannot be written."""

    pass


class ERR7_CantDoWithModalWindows(St7BaseException):
    """Operation cannot be performed when modal dialogs are open."""

    pass


class ERR7_CantGenerateFillet(St7BaseException):
    """Cannot generate fillet - points must be co-planar."""

    pass


class ERR7_CaseNameAlreadyExists(St7BaseException):
    """The specified case name already exists."""

    pass


class ERR7_CavityFluidNotConstBulk(St7BaseException):
    """The specified ID is not a Constant Bulk Modulus type."""

    pass


class ERR7_CavityFluidNotIdealGas(St7BaseException):
    """The specified ID is not an Ideal Gas type."""

    pass


class ERR7_CombinationDoesNotExist(St7BaseException):
    """The specified combination does not exist."""

    pass


class ERR7_CommentDoesNotExist(St7BaseException):
    """The specified comment does not exist."""

    pass


class ERR7_CompositesModuleNotLicensed(St7BaseException):
    """The Composites Module is not licensed."""

    pass


class ERR7_ContourFileNotLoaded(St7BaseException):
    """A contour file is not loaded."""

    pass


class ERR7_CouldNotCreateModelWindow(St7BaseException):
    """The model window could not be created."""

    pass


class ERR7_CouldNotDestroyModelWindow(St7BaseException):
    """The model window could not be destroyed."""

    pass


class ERR7_CouldNotSaveAnimationFile(St7BaseException):
    """An error occurred while saving the animation file."""

    pass


class ERR7_CouldNotShowModelWindow(St7BaseException):
    """The model window could not be displayed."""

    pass


class ERR7_CreepIDAlreadyExists(St7BaseException):
    """The specified creep definition ID already exists."""

    pass


class ERR7_DataNotFound(St7BaseException):
    """Data not found."""

    pass


class ERR7_DynamicsSolverModuleNotLicensed(St7BaseException):
    """The Dynamics Solver Module is not licensed."""

    pass


class ERR7_EquationDoesNotExist(St7BaseException):
    """The specified equation does not exist."""

    pass


class ERR7_ErrorCreatingImage(St7BaseException):
    """Unknown error has occurred while attempting to create image."""

    pass


class ERR7_ExceededMaxNumColumns(St7BaseException):
    """The maximum number of columns was exceeded."""

    pass


class ERR7_ExceededMaxNumCombEnvelopes(St7BaseException):
    """The maximum number of combination envelopes was exceeded."""

    pass


class ERR7_ExceededMaxNumCombResFiles(St7BaseException):
    """The maximum number of combination result files was exceeded."""

    pass


class ERR7_ExceededMaxNumEnvelopeSets(St7BaseException):
    """The maximum number of envelope sets was exceeded."""

    pass


class ERR7_ExceededMaxNumFactorsEnvelopes(St7BaseException):
    """The maximum number of factors envelopes was exceeded."""

    pass


class ERR7_ExceededMaxNumLimitEnvelopes(St7BaseException):
    """The maximum number of limit envelopes was exceeded."""

    pass


class ERR7_ExceededMaxNumLoadPathTemplates(St7BaseException):
    """The maximum number of load path templates was exceeded."""

    pass


class ERR7_ExceededMaxNumLoadPathVehicles(St7BaseException):
    """The maximum number of vehicles was exceeded."""

    pass


class ERR7_ExceededMaxNumNodeHistory(St7BaseException):
    """The maximum number of node history definitions was exceeded."""

    pass


class ERR7_ExceededMaxNumPlies(St7BaseException):
    """The maximum number of plies was exceeded."""

    pass


class ERR7_ExceededMaxNumRows(St7BaseException):
    """The maximum number of rows was exceeded."""

    pass


class ERR7_ExceededMaxNumSpectralCases(St7BaseException):
    """The maximum number of spectral cases was exceeded."""

    pass


class ERR7_ExceededMaxNumStages(St7BaseException):
    """The maximum number of stages was exceeded."""

    pass


class ERR7_ExceededResultCase(St7BaseException):
    """The requested result case does not exist."""

    pass


class ERR7_ExceededTotal(St7BaseException):
    """The total number of entities was exceeded."""

    pass


class ERR7_FileAlreadyOpen(St7BaseException):
    """The file is already open."""

    pass


class ERR7_FileIsNewer(St7BaseException):
    """The file was created with a later release."""

    pass


class ERR7_FileIsProtected(St7BaseException):
    """The file is encrypted and cannot be opened."""

    pass


class ERR7_FileNotFound(St7BaseException):
    """File not found."""

    pass


class ERR7_FileNotOpen(St7BaseException):
    """The file is not open."""

    pass


class ERR7_FileNotSt7(St7BaseException):
    """The file is not an St7 file."""

    pass


class ERR7_FilesStillOpen(St7BaseException):
    """There are files still open."""

    pass


class ERR7_FreeEdgesFound(St7BaseException):
    """The selected plate hull contains free edges."""

    pass


class ERR7_FunctionNotSupported(St7BaseException):
    """Function no longer supported. []"""

    pass


class ERR7_FunctionalityNotAvailable(St7BaseException):
    """The requested function is not active in this instance of St7API."""

    pass


class ERR7_GroupIdDoesNotExist(St7BaseException):
    """Group ID does not exist."""

    pass


class ERR7_IncompatibleCriterionCombination(St7BaseException):
    """Incompatible yield criterion combination."""

    pass


class ERR7_IncompatibleMaterialCombination(St7BaseException):
    """Incompatible material combination."""

    pass


class ERR7_IncompatibleResultFile(St7BaseException):
    """The current result file is incompatible with the requested result."""

    pass


class ERR7_IncompatibleSections(St7BaseException):
    """The specified beam properties cannot be interpolated."""

    pass


class ERR7_IncompatibleTableType(St7BaseException):
    """The specified table is incompatible with the selected table type."""

    pass


class ERR7_IncrementDoesNotExist(St7BaseException):
    """The specified increment does not exist."""

    pass


class ERR7_InsituCalculationFailed(St7BaseException):
    """In-situ calculation failed."""

    pass


class ERR7_InsufficientFrames(St7BaseException):
    """The specified number of frames is not sufficient to generate an animation."""

    pass


class ERR7_IntersectionNotFound(St7BaseException):
    """Intersection not found."""

    pass


class ERR7_InvalidAlphaTempType(St7BaseException):
    """The specified alpha vs temperature type is not valid"""

    pass


class ERR7_InvalidAnimationFile(St7BaseException):
    """The file is not a valid animation file."""

    pass


class ERR7_InvalidAnimationMode(St7BaseException):
    """The specified animation mode is not valid."""

    pass


class ERR7_InvalidAnimationType(St7BaseException):
    """The specified animation file type is not valid."""

    pass


class ERR7_InvalidAnsysArrayStatus(St7BaseException):
    """The specified ANSYS array status is not valid."""

    pass


class ERR7_InvalidAnsysEndReleaseOption(St7BaseException):
    """The specified ANSYS end release option is not valid."""

    pass


class ERR7_InvalidAnsysExportFormat(St7BaseException):
    """The specified ANSYS export format is not valid."""

    pass


class ERR7_InvalidAnsysExportUnits(St7BaseException):
    """The specified ANSYS export units is not valid."""

    pass


class ERR7_InvalidAnsysImportFormat(St7BaseException):
    """The specified ANSYS import format is not valid."""

    pass


class ERR7_InvalidArcLength(St7BaseException):
    """The specified arc length is not valid."""

    pass


class ERR7_InvalidAttachConnectionType(St7BaseException):
    """The specified attachment connection type is not valid."""

    pass


class ERR7_InvalidAttachPartsParams(St7BaseException):
    """Invalid attach parts parameters."""

    pass


class ERR7_InvalidAttachmentDirection(St7BaseException):
    """The specified attachment direction is not valid."""

    pass


class ERR7_InvalidAttachmentType(St7BaseException):
    """The specified attachment type is not valid."""

    pass


class ERR7_InvalidAttributeSetting(St7BaseException):
    """The specified attribute data is not valid."""

    pass


class ERR7_InvalidAttributeType(St7BaseException):
    """The specified attribute type is not valid."""

    pass


class ERR7_InvalidAveragingOption(St7BaseException):
    """The specified averaging option is not valid."""

    pass


class ERR7_InvalidAxis(St7BaseException):
    """The specified axis is not valid."""

    pass


class ERR7_InvalidAxisSystem(St7BaseException):
    """The specified axis system is not valid."""

    pass


class ERR7_InvalidBGLData(St7BaseException):
    """The section could not be generated from the library."""

    pass


class ERR7_InvalidBackgroundMode(St7BaseException):
    """The specified background mode is not valid."""

    pass


class ERR7_InvalidBaseExcitationType(St7BaseException):
    """The specified base excitation type is not valid."""

    pass


class ERR7_InvalidBeamAxisType(St7BaseException):
    """The specified beam axis type is not valid."""

    pass


class ERR7_InvalidBeamDir(St7BaseException):
    """The specified beam direction is not valid."""

    pass


class ERR7_InvalidBeamEnd(St7BaseException):
    """The specified beam end is not valid."""

    pass


class ERR7_InvalidBeamExtrudeTarget(St7BaseException):
    """The specified extrude beams to target is not valid."""

    pass


class ERR7_InvalidBeamLoadType(St7BaseException):
    """The specified load type is not valid."""

    pass


class ERR7_InvalidBeamPosition(St7BaseException):
    """Invalid beam position."""

    pass


class ERR7_InvalidBeamSectionType(St7BaseException):
    """The specified beam section type is not valid."""

    pass


class ERR7_InvalidBeamType(St7BaseException):
    """The specified beam type is not valid."""

    pass


class ERR7_InvalidBrickFace(St7BaseException):
    """The specified brick face is not valid."""

    pass


class ERR7_InvalidBrickIntegrationPoints(St7BaseException):
    """One or more specified integration points are not valid (Range is 1..3)."""

    pass


class ERR7_InvalidCementHardeningType(St7BaseException):
    """The specified cement hardening type is not valid."""

    pass


class ERR7_InvalidCollectionID(St7BaseException):
    """The specified collection ID is not valid."""

    pass


class ERR7_InvalidCombEnvelope(St7BaseException):
    """The specified combination envelope is not valid."""

    pass


class ERR7_InvalidCombEnvelopeAccType(St7BaseException):
    """The specified combination envelope accumulation type is not valid."""

    pass


class ERR7_InvalidCombEnvelopeType(St7BaseException):
    """The specified combination envelope type is not valid."""

    pass


class ERR7_InvalidCombResFile(St7BaseException):
    """The specified combination result file is not valid."""

    pass


class ERR7_InvalidCombinationCaseNumber(St7BaseException):
    """The specified load case combination number is not valid."""

    pass


class ERR7_InvalidComponent(St7BaseException):
    """The specified component is not valid."""

    pass


class ERR7_InvalidConnectionType(St7BaseException):
    """The specified connection type is not valid."""

    pass


class ERR7_InvalidContactSubType(St7BaseException):
    """The specified contact subtype is not valid."""

    pass


class ERR7_InvalidContactType(St7BaseException):
    """The specified contact type is not valid."""

    pass


class ERR7_InvalidContactYieldType(St7BaseException):
    """The specified contact yield type is not valid."""

    pass


class ERR7_InvalidContourFileIndex(St7BaseException):
    """The specified file index is not valid."""

    pass


class ERR7_InvalidContourIndex(St7BaseException):
    """The specified contour index is not valid."""

    pass


class ERR7_InvalidCoupleType(St7BaseException):
    """The specified couple type is not valid."""

    pass


class ERR7_InvalidCreepFunctionType(St7BaseException):
    """The specified creep function/chain type is not valid."""

    pass


class ERR7_InvalidCreepHardeningLaw(St7BaseException):
    """The specified creep hardening law is not valid."""

    pass


class ERR7_InvalidCreepID(St7BaseException):
    """The specified creep definition ID is not valid."""

    pass


class ERR7_InvalidCreepLaw(St7BaseException):
    """The specified creep law is not valid."""

    pass


class ERR7_InvalidCreepShrinkageType(St7BaseException):
    """The specified creep shrinkage type is not valid."""

    pass


class ERR7_InvalidCreepViscoChainRow(St7BaseException):
    """The specified creep viscoelastic data row is not valid."""

    pass


class ERR7_InvalidCurvedPipesAsOption(St7BaseException):
    """The specified curved pipes option is not valid."""

    pass


class ERR7_InvalidCutoffType(St7BaseException):
    """The specified cutoff type is not valid."""

    pass


class ERR7_InvalidDLLsPresent(St7BaseException):
    """SlvPanel.dll and/or St6List.dll are not compatible with St7API.dll."""

    pass


class ERR7_InvalidDXFBeamOption(St7BaseException):
    """The specified DXF beam option is not valid."""

    pass


class ERR7_InvalidDXFPlateOption(St7BaseException):
    """The specified DXF plate option is not valid."""

    pass


class ERR7_InvalidDampingType(St7BaseException):
    """The specified damping type is not valid."""

    pass


class ERR7_InvalidDefaultsMode(St7BaseException):
    """The specified defaults mode is not valid."""

    pass


class ERR7_InvalidDetachMode(St7BaseException):
    """The specified detach mode is not valid."""

    pass


class ERR7_InvalidDiagramAxis(St7BaseException):
    """The specified diagram axis is not valid."""

    pass


class ERR7_InvalidDigits(St7BaseException):
    """The specified number of digits is not valid."""

    pass


class ERR7_InvalidDirection(St7BaseException):
    """The specified direction is not valid."""

    pass


class ERR7_InvalidDirectionVector(St7BaseException):
    """The specified direction vector is not valid."""

    pass


class ERR7_InvalidDisplayOptionsPath(St7BaseException):
    """The configuration file folder is not valid."""

    pass


class ERR7_InvalidDivisionParameters(St7BaseException):
    """The specified subdivisions are not valid."""

    pass


class ERR7_InvalidDivisionTargets(St7BaseException):
    """The specified target types are not valid."""

    pass


class ERR7_InvalidDivisions(St7BaseException):
    """The specified number of divisions is not valid."""

    pass


class ERR7_InvalidDrawParameters(St7BaseException):
    """Invalid entity display parameters."""

    pass


class ERR7_InvalidDuplicateFaceType(St7BaseException):
    """The specified duplicate face type is not valid."""

    pass


class ERR7_InvalidEdgeTolerance(St7BaseException):
    """The specified edge tolerance is not valid."""

    pass


class ERR7_InvalidEntity(St7BaseException):
    """Invalid entity."""

    pass


class ERR7_InvalidEntityContourFileType(St7BaseException):
    """The specified contour file type is not valid."""

    pass


class ERR7_InvalidEntityID(St7BaseException):
    """The specified entity ID is not valid."""

    pass


class ERR7_InvalidEntityNodes(St7BaseException):
    """An invalid number of nodes was specified."""

    pass


class ERR7_InvalidEntityNumber(St7BaseException):
    """The specified entity number is not valid."""

    pass


class ERR7_InvalidEntitySet(St7BaseException):
    """The requested entity set is not valid."""

    pass


class ERR7_InvalidEnvelopeSet(St7BaseException):
    """The specified envelope set is not valid."""

    pass


class ERR7_InvalidEnvelopeSetType(St7BaseException):
    """The specified envelope set type is not valid."""

    pass


class ERR7_InvalidErrorCode(St7BaseException):
    """An invalid error code was requested."""

    pass


class ERR7_InvalidExponentFormat(St7BaseException):
    """The specified exponent format is not valid."""

    pass


class ERR7_InvalidExportParameters(St7BaseException):
    """One or more export parameters are not valid."""

    pass


class ERR7_InvalidFaceFromBeamPolygonParameters(St7BaseException):
    """Invalid face from beam polygon parameters."""

    pass


class ERR7_InvalidFaceSurface(St7BaseException):
    """The specified geometry face surface is not valid."""

    pass


class ERR7_InvalidFactorsEnvelope(St7BaseException):
    """The specified factors envelope is not valid."""

    pass


class ERR7_InvalidFactorsEnvelopeType(St7BaseException):
    """The specified factors envelope type is not valid."""

    pass


class ERR7_InvalidFileName(St7BaseException):
    """The file name is not valid."""

    pass


class ERR7_InvalidFilePath(St7BaseException):
    """The file path is not valid."""

    pass


class ERR7_InvalidFileUnit(St7BaseException):
    """Invalid file unit."""

    pass


class ERR7_InvalidFontName(St7BaseException):
    """The specified font name is not valid."""

    pass


class ERR7_InvalidFreedomCase(St7BaseException):
    """Invalid freedom case."""

    pass


class ERR7_InvalidFreedomCaseType(St7BaseException):
    """The specified freedom case type is not valid."""

    pass


class ERR7_InvalidFrequencyType(St7BaseException):
    """The specified frequency type is not valid."""

    pass


class ERR7_InvalidGeometryAsOption(St7BaseException):
    """The specified geometry option is not valid."""

    pass


class ERR7_InvalidGeometryCavityLoop(St7BaseException):
    """The specified geometry face cavity loop is not valid."""

    pass


class ERR7_InvalidGeometryEdgeType(St7BaseException):
    """The specified geometry edge type is not valid."""

    pass


class ERR7_InvalidGeometryFormatProtocol(St7BaseException):
    """The specified geometry format/protocol is not valid."""

    pass


class ERR7_InvalidGradeRatio(St7BaseException):
    """Grade ratio must be greater than zero and less than one."""

    pass


class ERR7_InvalidGradeType(St7BaseException):
    """The specified grade type is not valid."""

    pass


class ERR7_InvalidGravityDirection(St7BaseException):
    """Invalid gravity direction."""

    pass


class ERR7_InvalidHRAMode(St7BaseException):
    """The specified harmonic mode type is not valid."""

    pass


class ERR7_InvalidHardeningType(St7BaseException):
    """The specified hardening type is not valid."""

    pass


class ERR7_InvalidHarmonicLoadType(St7BaseException):
    """The specified harmonic load type is not valid."""

    pass


class ERR7_InvalidImageDimensions(St7BaseException):
    """The specified image dimensions are not valid."""

    pass


class ERR7_InvalidImageType(St7BaseException):
    """The specified image type is not valid."""

    pass


class ERR7_InvalidImportExportMode(St7BaseException):
    """The specified import/export mode is not valid."""

    pass


class ERR7_InvalidIndex(St7BaseException):
    """The requested index is outside the allowable range."""

    pass


class ERR7_InvalidInfluenceFile(St7BaseException):
    """The specified influence results file is not valid."""

    pass


class ERR7_InvalidInitialCaseNumber(St7BaseException):
    """The specified initial case number is not valid."""

    pass


class ERR7_InvalidInitialConditionsType(St7BaseException):
    """The specified initial conditions type is not valid."""

    pass


class ERR7_InvalidInitialFile(St7BaseException):
    """The specified initial file is not valid."""

    pass


class ERR7_InvalidInsituRunMode(St7BaseException):
    """The specified run mode is not valid."""

    pass


class ERR7_InvalidIterationNumber(St7BaseException):
    """The specified number of iterations is not valid."""

    pass


class ERR7_InvalidK0Expression(St7BaseException):
    """Invalid K0 expression."""

    pass


class ERR7_InvalidK1Expression(St7BaseException):
    """Invalid K1 expression."""

    pass


class ERR7_InvalidLTAMethod(St7BaseException):
    """The specified linear transient solver method is not valid."""

    pass


class ERR7_InvalidLTASolutionType(St7BaseException):
    """The specified linear transient solver solution type is not valid."""

    pass


class ERR7_InvalidLaminateID(St7BaseException):
    """The specified laminate ID is not valid."""

    pass


class ERR7_InvalidLayoutID(St7BaseException):
    """The specified layout ID is not valid."""

    pass


class ERR7_InvalidLength(St7BaseException):
    """The specified length is not valid."""

    pass


class ERR7_InvalidLibraryID(St7BaseException):
    """The specified library ID is not valid."""

    pass


class ERR7_InvalidLibraryItemID(St7BaseException):
    """The specified library item ID is not valid."""

    pass


class ERR7_InvalidLibraryItemName(St7BaseException):
    """The specified library item name is not valid."""

    pass


class ERR7_InvalidLibraryName(St7BaseException):
    """The specified library name is not valid."""

    pass


class ERR7_InvalidLibraryPath(St7BaseException):
    """The library folder is not valid."""

    pass


class ERR7_InvalidLibraryType(St7BaseException):
    """The specified library type is not valid."""

    pass


class ERR7_InvalidLimitEnvelope(St7BaseException):
    """The specified limit envelope is not valid."""

    pass


class ERR7_InvalidLimitEnvelopeType(St7BaseException):
    """The specified limit envelope type is not valid."""

    pass


class ERR7_InvalidLineDefinition(St7BaseException):
    """A valid extrusion line could not be formed from the specified entity set."""

    pass


class ERR7_InvalidLineID(St7BaseException):
    """The specified line ID is not valid."""

    pass


class ERR7_InvalidLinePoints(St7BaseException):
    """The specified line points are not valid."""

    pass


class ERR7_InvalidLinkData(St7BaseException):
    """The specified link data is not valid."""

    pass


class ERR7_InvalidLinkTarget(St7BaseException):
    """The specified link target is not valid."""

    pass


class ERR7_InvalidLinkType(St7BaseException):
    """The specified link type is not valid."""

    pass


class ERR7_InvalidLoadCase(St7BaseException):
    """Invalid load case."""

    pass


class ERR7_InvalidLoadCaseFilePath(St7BaseException):
    """The ANSYS load case file folder is not valid."""

    pass


class ERR7_InvalidLoadCaseType(St7BaseException):
    """The specified load case type is not valid."""

    pass


class ERR7_InvalidLoadID(St7BaseException):
    """The specified load ID is not valid."""

    pass


class ERR7_InvalidLoadPath(St7BaseException):
    """The specified load path is not valid."""

    pass


class ERR7_InvalidLoadPathID(St7BaseException):
    """The specified load path ID is not valid."""

    pass


class ERR7_InvalidLoadPathLane(St7BaseException):
    """The specified load path template lane is not valid."""

    pass


class ERR7_InvalidLoadPathLaneFactorType(St7BaseException):
    """The specified load path template multi lane factor type is not valid."""

    pass


class ERR7_InvalidLoadPathShape(St7BaseException):
    """The specified load path shape is not valid."""

    pass


class ERR7_InvalidLoadPathSurface(St7BaseException):
    """The specified load path surface is not valid."""

    pass


class ERR7_InvalidLoadPathTemplateID(St7BaseException):
    """The specified load path template ID is not valid."""

    pass


class ERR7_InvalidLoadPathVehicle(St7BaseException):
    """The specified load path template vehicle is not valid."""

    pass


class ERR7_InvalidLoadPathVehicleInstance(St7BaseException):
    """The specified load path template vehicle instance type is not valid."""

    pass


class ERR7_InvalidMarkerLineThickness(St7BaseException):
    """The specified marker line thickness is not valid."""

    pass


class ERR7_InvalidMarkerSize(St7BaseException):
    """The specified marker size is not valid."""

    pass


class ERR7_InvalidMarkerStyle(St7BaseException):
    """The specified marker style is not valid."""

    pass


class ERR7_InvalidMarkerType(St7BaseException):
    """The specified marker type is not valid."""

    pass


class ERR7_InvalidMaterialType(St7BaseException):
    """The specified material type is not valid."""

    pass


class ERR7_InvalidMatrixType(St7BaseException):
    """The specified matrix type is not valid."""

    pass


class ERR7_InvalidMeshPositionOnUCS(St7BaseException):
    """The specified UCS position is not valid."""

    pass


class ERR7_InvalidMirrorOption(St7BaseException):
    """The specified mirror option is not valid."""

    pass


class ERR7_InvalidMobilityType(St7BaseException):
    """The specified mobility type is not valid."""

    pass


class ERR7_InvalidModType(St7BaseException):
    """The specified time dependent modulus type is not valid."""

    pass


class ERR7_InvalidModalFile(St7BaseException):
    """The specified modal results file is not valid."""

    pass


class ERR7_InvalidModalLoadType(St7BaseException):
    """The specified modal load type is not valid."""

    pass


class ERR7_InvalidModalNodeReactType(St7BaseException):
    """The specified node reaction type is not valid."""

    pass


class ERR7_InvalidModeNumber(St7BaseException):
    """The specified mode number is not valid."""

    pass


class ERR7_InvalidMultiPointLink(St7BaseException):
    """The specified multi-point link is not valid."""

    pass


class ERR7_InvalidMultiPointType(St7BaseException):
    """The specified multi-point link type is not valid."""

    pass


class ERR7_InvalidMultiVariableCaseID(St7BaseException):
    """The specified multi variable influence case ID is not valid."""

    pass


class ERR7_InvalidMultiVariableType(St7BaseException):
    """The specified multi variable influence type is not valid."""

    pass


class ERR7_InvalidName(St7BaseException):
    """The specified name is not valid."""

    pass


class ERR7_InvalidNodeCoordinateKeepType(St7BaseException):
    """The specified node coordinate keep type is not valid."""

    pass


class ERR7_InvalidNodeExtrudeTarget(St7BaseException):
    """The specified extrude nodes to target is not valid."""

    pass


class ERR7_InvalidNumBeamStations(St7BaseException):
    """The specified number of beam stations is not valid."""

    pass


class ERR7_InvalidNumCopies(St7BaseException):
    """The specified number of copies is not valid."""

    pass


class ERR7_InvalidNumCutFaces(St7BaseException):
    """The specified number of cut faces must be 0, 1 or 2."""

    pass


class ERR7_InvalidNumLayers(St7BaseException):
    """The specified number of layers is not valid."""

    pass


class ERR7_InvalidNumMeshingLoops(St7BaseException):
    """The specified number of loops is not valid."""

    pass


class ERR7_InvalidNumModes(St7BaseException):
    """The requested number of modes is not valid."""

    pass


class ERR7_InvalidNumPathDivs(St7BaseException):
    """The specified number of path divisions is not valid."""

    pass


class ERR7_InvalidNumRepeats(St7BaseException):
    """The specified number of repeats is not valid."""

    pass


class ERR7_InvalidNumSteps(St7BaseException):
    """The specified number of steps is not valid."""

    pass


class ERR7_InvalidNumberOfEntries(St7BaseException):
    """The specified number of table entries is not valid."""

    pass


class ERR7_InvalidNumericStyle(St7BaseException):
    """The specified numeric format is not valid."""

    pass


class ERR7_InvalidOption(St7BaseException):
    """A specified option is not valid."""

    pass


class ERR7_InvalidOriginMethod(St7BaseException):
    """The specified origin method is not valid."""

    pass


class ERR7_InvalidP1P2(St7BaseException):
    """P1,P2 are not valid."""

    pass


class ERR7_InvalidP1P2P3(St7BaseException):
    """P1,P2,P3 are not valid."""

    pass


class ERR7_InvalidP1P2P3P4(St7BaseException):
    """P1,P2,P3,P4 are not valid."""

    pass


class ERR7_InvalidPLTarget(St7BaseException):
    """The specified points and lines target is not valid."""

    pass


class ERR7_InvalidPasteOption(St7BaseException):
    """One or more paste options are not valid."""

    pass


class ERR7_InvalidPatchType(St7BaseException):
    """The specified patch type is not valid."""

    pass


class ERR7_InvalidPatchTypeForPlate(St7BaseException):
    """The specified patch type is not valid for the selected element."""

    pass


class ERR7_InvalidPathDefinition(St7BaseException):
    """The path definition is not valid."""

    pass


class ERR7_InvalidPlane(St7BaseException):
    """The specified plane is not valid."""

    pass


class ERR7_InvalidPlaneID(St7BaseException):
    """The specified plane ID is not valid."""

    pass


class ERR7_InvalidPlanePoints(St7BaseException):
    """The specified plane points are not valid."""

    pass


class ERR7_InvalidPlateEdge(St7BaseException):
    """The specified plate edge is not valid."""

    pass


class ERR7_InvalidPlateSurface(St7BaseException):
    """The specified plate surface is not valid."""

    pass


class ERR7_InvalidPlateType(St7BaseException):
    """The specified plate type is not valid."""

    pass


class ERR7_InvalidPositionTableAxis(St7BaseException):
    """The specified position table axis is not valid."""

    pass


class ERR7_InvalidPositionType(St7BaseException):
    """The specified position type is not valid."""

    pass


class ERR7_InvalidPreLoadType(St7BaseException):
    """The specified pre-load type is not valid."""

    pass


class ERR7_InvalidProcessingMode(St7BaseException):
    """The specified processing mode is not valid."""

    pass


class ERR7_InvalidProjectFlag(St7BaseException):
    """The specified project flag is not valid."""

    pass


class ERR7_InvalidProjectionDirection(St7BaseException):
    """The specified projection direction is not valid."""

    pass


class ERR7_InvalidPropertyNumber(St7BaseException):
    """The specified property number is not valid."""

    pass


class ERR7_InvalidQuadraticAsOption(St7BaseException):
    """The specified quadratic option is not valid."""

    pass


class ERR7_InvalidR1R2(St7BaseException):
    """R1 must be greater than R2."""

    pass


class ERR7_InvalidR2(St7BaseException):
    """R2 is too large."""

    pass


class ERR7_InvalidRCLayers(St7BaseException):
    """The specified reinforcement layers are not valid."""

    pass


class ERR7_InvalidRadius(St7BaseException):
    """The specified radius is not valid."""

    pass


class ERR7_InvalidRayleighMode(St7BaseException):
    """The specified Rayleigh mode is not valid."""

    pass


class ERR7_InvalidReferenceNode(St7BaseException):
    """The specified displacement reference node is not valid."""

    pass


class ERR7_InvalidRegionalSettings(St7BaseException):
    """The API cannot load because the Regional Settings on your system are not valid."""

    pass


class ERR7_InvalidResOptsBaseMode(St7BaseException):
    """The specified base mode is not valid."""

    pass


class ERR7_InvalidResOptsNFADisp(St7BaseException):
    """The specified NFA displacement option is not valid."""

    pass


class ERR7_InvalidResOptsReactionLinkGNL(St7BaseException):
    """The specified reaction link GNL displacement option is not valid."""

    pass


class ERR7_InvalidResOptsRotationUnit(St7BaseException):
    """The specified rotation unit is not valid."""

    pass


class ERR7_InvalidResOptsStrainUnit(St7BaseException):
    """Invalid strain unit."""

    pass


class ERR7_InvalidResponseType(St7BaseException):
    """The response type specified is not valid."""

    pass


class ERR7_InvalidResponseVariable(St7BaseException):
    """The specified influence variable is not valid."""

    pass


class ERR7_InvalidResultCase(St7BaseException):
    """The requested result case is not valid."""

    pass


class ERR7_InvalidResultFile(St7BaseException):
    """The file is not a valid St7 result file."""

    pass


class ERR7_InvalidResultQuantity(St7BaseException):
    """The specified quantity is not valid."""

    pass


class ERR7_InvalidResultSubQuantity(St7BaseException):
    """The specified sub-quantity is not valid."""

    pass


class ERR7_InvalidResultType(St7BaseException):
    """The specified result type is not valid."""

    pass


class ERR7_InvalidResultsSign(St7BaseException):
    """The specified results sign is not valid."""

    pass


class ERR7_InvalidRigidPlane(St7BaseException):
    """The specified rigid plane is not valid."""

    pass


class ERR7_InvalidRubberModel(St7BaseException):
    """The specified rubber model is not valid."""

    pass


class ERR7_InvalidSTLBeamOption(St7BaseException):
    """The specified STL beam option is not valid."""

    pass


class ERR7_InvalidSTLFileFormat(St7BaseException):
    """The specified STL file format option is not valid."""

    pass


class ERR7_InvalidSTLGroupingOption(St7BaseException):
    """The specified STL grouping option is not valid."""

    pass


class ERR7_InvalidSTLPlateOption(St7BaseException):
    """The specified STL plate option is not valid."""

    pass


class ERR7_InvalidScaleAbout(St7BaseException):
    """The specified scale about option is not valid."""

    pass


class ERR7_InvalidScratchPath(St7BaseException):
    """The scratch folder is not valid."""

    pass


class ERR7_InvalidSectionParameters(St7BaseException):
    """The specified section parameters are not valid."""

    pass


class ERR7_InvalidSectionProperties(St7BaseException):
    """The specified section properties are not valid."""

    pass


class ERR7_InvalidSegmentsPerCircle(St7BaseException):
    """The specified number of segments per circle is not valid."""

    pass


class ERR7_InvalidSeismicCase(St7BaseException):
    """The specified seismic case is not valid."""

    pass


class ERR7_InvalidSelectionEndEdgeFace(St7BaseException):
    """The specified end, edge or face is not valid."""

    pass


class ERR7_InvalidSolverMode(St7BaseException):
    """The specified solver mode is not valid."""

    pass


class ERR7_InvalidSolverParameter(St7BaseException):
    """The specified solver parameter is not valid."""

    pass


class ERR7_InvalidSolverPath(St7BaseException):
    """The solver folder is not valid."""

    pass


class ERR7_InvalidSolverScheme(St7BaseException):
    """The specified solver storage scheme is not valid."""

    pass


class ERR7_InvalidSortMethod(St7BaseException):
    """The specified sort method is not valid."""

    pass


class ERR7_InvalidSortOption(St7BaseException):
    """The specified sort option is not valid."""

    pass


class ERR7_InvalidSourceAction(St7BaseException):
    """The specified source action is not valid."""

    pass


class ERR7_InvalidSpectralCase(St7BaseException):
    """The specified spectral case is not valid."""

    pass


class ERR7_InvalidSpectrumType(St7BaseException):
    """The specified spectrum type is not valid."""

    pass


class ERR7_InvalidSplitData(St7BaseException):
    """The specified split data is not valid."""

    pass


class ERR7_InvalidSplitRatio(St7BaseException):
    """The specified split ratio is not valid."""

    pass


class ERR7_InvalidSt7ExportFormat(St7BaseException):
    """The specified ST7 export format is not valid."""

    pass


class ERR7_InvalidStaadCountryCodeOption(St7BaseException):
    """The specified STAAD country code option is not valid."""

    pass


class ERR7_InvalidStaadForceUnit(St7BaseException):
    """The specified STAAD force unit is not valid."""

    pass


class ERR7_InvalidStaadLengthUnit(St7BaseException):
    """The specified STAAD length unit is not valid."""

    pass


class ERR7_InvalidStartEndTimes(St7BaseException):
    """The specified start and end times are not valid."""

    pass


class ERR7_InvalidStringID(St7BaseException):
    """The specified string ID is not valid."""

    pass


class ERR7_InvalidSurfaceMeshTargetType(St7BaseException):
    """The specified plate element target is not valid."""

    pass


class ERR7_InvalidTableID(St7BaseException):
    """The specified table ID is not valid."""

    pass


class ERR7_InvalidTableName(St7BaseException):
    """The specified table name is not valid."""

    pass


class ERR7_InvalidTableRow(St7BaseException):
    """The specified table row is not valid."""

    pass


class ERR7_InvalidTableSetting(St7BaseException):
    """The specified table setting is not valid."""

    pass


class ERR7_InvalidTableType(St7BaseException):
    """The specified table type is not valid."""

    pass


class ERR7_InvalidTaperAxis(St7BaseException):
    """The specified taper axis is not valid."""

    pass


class ERR7_InvalidTaperRatio(St7BaseException):
    """The specified taper ratios are not valid."""

    pass


class ERR7_InvalidTaperType(St7BaseException):
    """The specified taper type is not valid."""

    pass


class ERR7_InvalidTempDependenceType(St7BaseException):
    """The specified temperature dependence type is not valid."""

    pass


class ERR7_InvalidTemperatureType(St7BaseException):
    """The specified temperature type is not valid."""

    pass


class ERR7_InvalidTimeRow(St7BaseException):
    """The specified time step row is not valid."""

    pass


class ERR7_InvalidTimeUnit(St7BaseException):
    """The specified time unit type is not valid."""

    pass


class ERR7_InvalidTolerance(St7BaseException):
    """The specified tolerance is not valid."""

    pass


class ERR7_InvalidToleranceType(St7BaseException):
    """The specified tolerance type is not valid."""

    pass


class ERR7_InvalidToolOptsCopyOptions(St7BaseException):
    """The specified copy settings are not valid."""

    pass


class ERR7_InvalidToolOptsSubdivideOptions(St7BaseException):
    """The specified subdivide settings are not valid."""

    pass


class ERR7_InvalidToolOptsZipOptions(St7BaseException):
    """The specified zip settings are not valid."""

    pass


class ERR7_InvalidTransientTempType(St7BaseException):
    """The specified transient temperature input type is not valid."""

    pass


class ERR7_InvalidTrigType(St7BaseException):
    """The specified trigonometric type is not valid."""

    pass


class ERR7_InvalidUCSID(St7BaseException):
    """The UCS ID specified is not valid."""

    pass


class ERR7_InvalidUCSIndex(St7BaseException):
    """The specified UCS index is not valid."""

    pass


class ERR7_InvalidUCSType(St7BaseException):
    """The UCS type specified is not valid."""

    pass


class ERR7_InvalidUVPos(St7BaseException):
    """The u-v position specified is not valid."""

    pass


class ERR7_InvalidUnits(St7BaseException):
    """The unit type specified is not valid."""

    pass


class ERR7_InvalidUserEquation(St7BaseException):
    """The specified user equation is not valid."""

    pass


class ERR7_InvalidVectorComponents(St7BaseException):
    """The specified vector component is not valid."""

    pass


class ERR7_InvalidVertexMeshSize(St7BaseException):
    """The specified vertex mesh size is not valid."""

    pass


class ERR7_InvalidVertexType(St7BaseException):
    """The specified vertex type is not valid."""

    pass


class ERR7_InvalidWindowDimensions(St7BaseException):
    """The specified window dimensions are not valid."""

    pass


class ERR7_InvalidWindowMode(St7BaseException):
    """The specified window mode is not valid."""

    pass


class ERR7_LaminateIDAlreadyExists(St7BaseException):
    """The specified laminate ID already exists."""

    pass


class ERR7_LaminateNameAlreadyExists(St7BaseException):
    """The specified laminate name already exists."""

    pass


class ERR7_LayoutIDAlreadyExists(St7BaseException):
    """The specified concrete layout ID already exists."""

    pass


class ERR7_LinkNotAttachment(St7BaseException):
    """The specified link is not an attachment link."""

    pass


class ERR7_LinkNotCoupling(St7BaseException):
    """The specified link is not a coupling link."""

    pass


class ERR7_LinkNotMasterSlave(St7BaseException):
    """The specified link is not a master-slave link."""

    pass


class ERR7_LinkNotMultiPoint(St7BaseException):
    """The specified link is not a multi-point link."""

    pass


class ERR7_LinkNotPinned(St7BaseException):
    """The specified link is not a pinned link."""

    pass


class ERR7_LinkNotRigid(St7BaseException):
    """The specified link is not a rigid link."""

    pass


class ERR7_LinkNotSectorSymmetry(St7BaseException):
    """The specified link is not a sector symmetry link."""

    pass


class ERR7_LinkNotShrink(St7BaseException):
    """The specified link is not a shrink link."""

    pass


class ERR7_LinkNotTwoPoint(St7BaseException):
    """The specified link is not a 2-point link."""

    pass


class ERR7_LoadPathIDAlreadyExists(St7BaseException):
    """The specified load path ID already exists."""

    pass


class ERR7_LoadPathTemplateIDAlreadyExists(St7BaseException):
    """The specified load path template ID already exists."""

    pass


class ERR7_LoginExceeded(St7BaseException):
    """Cannot obtain API licence as maximum number of licences are in use."""

    pass


class ERR7_MarkerNotFound(St7BaseException):
    """The specified entity does not have a marker."""

    pass


class ERR7_MaterialIsUserDefined(St7BaseException):
    """The specified property uses a user defined material model."""

    pass


class ERR7_MaterialNotAnisotropic(St7BaseException):
    """The specified property does not use an anisotropic material model."""

    pass


class ERR7_MaterialNotFluid(St7BaseException):
    """The specified property does not use a fluid material model."""

    pass


class ERR7_MaterialNotIsotropic(St7BaseException):
    """The specified property does not use an isotropic material model."""

    pass


class ERR7_MaterialNotLaminate(St7BaseException):
    """The specified property does not use a laminate material model."""

    pass


class ERR7_MaterialNotOrthotropic(St7BaseException):
    """The specified property does not use an orthotropic material model."""

    pass


class ERR7_MaterialNotRubber(St7BaseException):
    """The specified property does not use a rubber material model."""

    pass


class ERR7_MaterialNotSoil(St7BaseException):
    """The specified property does not use a soil material model."""

    pass


class ERR7_MaterialNotUserDefined(St7BaseException):
    """The specified property does not use a user-defined material model."""

    pass


class ERR7_MeshingErrors(St7BaseException):
    """Meshing has generated an error."""

    pass


class ERR7_ModelMixesAxiNonAxi(St7BaseException):
    """Model mixes axisymmetric elements with non-axisymmetric elements."""

    pass


class ERR7_ModelWindowWasNotCreated(St7BaseException):
    """The model window has not been created."""

    pass


class ERR7_ModelWindowWasNotShowing(St7BaseException):
    """The model window was not showing."""

    pass


class ERR7_MovingLoadModuleNotLicensed(St7BaseException):
    """The Moving Load Module is not licensed."""

    pass


class ERR7_NoActiveResponseVariables(St7BaseException):
    """No active response variables found for influence combination."""

    pass


class ERR7_NoElementsOnLoadPaths(St7BaseException):
    """No elements on load paths found for influence combination."""

    pass


class ERR7_NoError(St7BaseException):
    """No error."""

    pass


class ERR7_NoInfluenceCombinationsDefined(St7BaseException):
    """There are no influence combinations defined."""

    pass


class ERR7_NoLoadPathsFound(St7BaseException):
    """No load paths found for influence combination."""

    pass


class ERR7_NoMultiVariableInfluenceCases(St7BaseException):
    """The model contains no multi variable influence cases."""

    pass


class ERR7_NoPlateElements(St7BaseException):
    """The model contains no plate elements."""

    pass


class ERR7_NoResponsesFound(St7BaseException):
    """No response found for influence combination."""

    pass


class ERR7_NoSoilElementsFound(St7BaseException):
    """No soil elements found."""

    pass


class ERR7_NodeHistoryDoesNotExist(St7BaseException):
    """The specified node history does not exist."""

    pass


class ERR7_NonlinearSolverModuleNotLicensed(St7BaseException):
    """The Nonlinear Solver Module is not licensed."""

    pass


class ERR7_NotFrequencyTable(St7BaseException):
    """The specified table is not a frequency table."""

    pass


class ERR7_NothingSelected(St7BaseException):
    """Nothing is selected."""

    pass


class ERR7_OnlyOneFreedomCase(St7BaseException):
    """The model contains only one freedom case, which cannot be deleted."""

    pass


class ERR7_OnlyOneLoadCase(St7BaseException):
    """The model contains only one load case, which cannot be deleted."""

    pass


class ERR7_OperationFailed(St7BaseException):
    """The tool operation has failed."""

    pass


class ERR7_OperationUserTerminated(St7BaseException):
    """Operation terminated by the user."""

    pass


class ERR7_PlateDoesNotHaveLayers(St7BaseException):
    """The specified plate property type does not support layers"""

    pass


class ERR7_PlateDoesNotHaveThickness(St7BaseException):
    """The specified plate does not have a valid thickness."""

    pass


class ERR7_PlyDoesNotExist(St7BaseException):
    """The specified ply does not exist."""

    pass


class ERR7_PropertyAlreadyExists(St7BaseException):
    """The specified property already exists."""

    pass


class ERR7_PropertyNotBeam(St7BaseException):
    """The specified beam is not of a beam type."""

    pass


class ERR7_PropertyNotCable(St7BaseException):
    """The specified beam is not a cable."""

    pass


class ERR7_PropertyNotConnectionBeam(St7BaseException):
    """The specified beam is not a connection beam."""

    pass


class ERR7_PropertyNotCutOffBar(St7BaseException):
    """The specified beam is not a cutoff bar."""

    pass


class ERR7_PropertyNotPipe(St7BaseException):
    """The specified beam is not a pipe."""

    pass


class ERR7_PropertyNotPointContact(St7BaseException):
    """The specified beam is not a point contact."""

    pass


class ERR7_PropertyNotSpring(St7BaseException):
    """The specified beam is not a spring."""

    pass


class ERR7_PropertyNotTruss(St7BaseException):
    """The specified beam is not a truss."""

    pass


class ERR7_PropertyNotUserDefinedBeam(St7BaseException):
    """The specified beam is not a user defined beam."""

    pass


class ERR7_PseudoTimeNotDefined(St7BaseException):
    """Pseudo time is not defined."""

    pass


class ERR7_RCModuleNotLicensed(St7BaseException):
    """The RC Module is not licensed."""

    pass


class ERR7_RayleighNotApplicable(St7BaseException):
    """Rayleigh damping not applicable to property of this type."""

    pass


class ERR7_ReducedAnimation(St7BaseException):
    """Insufficient memory for complete animation."""

    pass


class ERR7_ResFileAlreadyOpen(St7BaseException):
    """The result file is already open."""

    pass


class ERR7_ResFileAssociationNotAllowed(St7BaseException):
    """Load and freedom case association is not supported by this result file type."""

    pass


class ERR7_ResFileCantClearQuantity(St7BaseException):
    """The specified quantity must always exist in a result file."""

    pass


class ERR7_ResFileCantSave(St7BaseException):
    """The result file cannot be saved."""

    pass


class ERR7_ResFileContainsNoElements(St7BaseException):
    """The model does not contain any elements."""

    pass


class ERR7_ResFileContainsNoNodes(St7BaseException):
    """The model does not contain any nodes."""

    pass


class ERR7_ResFileDoesNotHaveEntity(St7BaseException):
    """The model does not contain this entity."""

    pass


class ERR7_ResFileIncompatibleQuantity(St7BaseException):
    """The specified quantity is not compatible with the result file type."""

    pass


class ERR7_ResFileInvalidCase(St7BaseException):
    """The specified result case is not valid."""

    pass


class ERR7_ResFileInvalidNumCases(St7BaseException):
    """The specified number of result cases is not valid."""

    pass


class ERR7_ResFileInvalidQuantity(St7BaseException):
    """The specified result quantity is not valid."""

    pass


class ERR7_ResFileNotOpen(St7BaseException):
    """The result file is not open."""

    pass


class ERR7_ResFileQuantityNotExist(St7BaseException):
    """The result file does not contain the specified result quantity."""

    pass


class ERR7_ResFileUnsupportedType(St7BaseException):
    """The specified solution type is not supported."""

    pass


class ERR7_ResultCaseNotInertiaRelief(St7BaseException):
    """The specified result case is not an Inertia Relief case."""

    pass


class ERR7_ResultFileIsOpen(St7BaseException):
    """A result file is open."""

    pass


class ERR7_ResultFileNotOpen(St7BaseException):
    """The result file is not open."""

    pass


class ERR7_ResultIsNotAvailable(St7BaseException):
    """The result is not available."""

    pass


class ERR7_ResultQuantityNotAvailable(St7BaseException):
    """The result quantity requested is not available."""

    pass


class ERR7_SectionCannotBeMirrored(St7BaseException):
    """The section cannot be mirrored."""

    pass


class ERR7_SectionNotBGL(St7BaseException):
    """The specified beam property is not a BGL section."""

    pass


class ERR7_SoilTypeNotCC(St7BaseException):
    """The specified property does not use a Cam-Clay soil material model."""

    pass


class ERR7_SoilTypeNotDC(St7BaseException):
    """The specified property does not use a Duncan-Chang soil material model."""

    pass


class ERR7_SoilTypeNotDP(St7BaseException):
    """The specified property does not use a Drucker-Prager soil material model."""

    pass


class ERR7_SoilTypeNotLS(St7BaseException):
    """The specified property does not use a linear elastic soil material model."""

    pass


class ERR7_SoilTypeNotMC(St7BaseException):
    """The specified property does not use a Mohr-Coulomb soil material model."""

    pass


class ERR7_SolverStillRunning(St7BaseException):
    """There are solvers still running."""

    pass


class ERR7_SparseSolverModuleNotLicensed(St7BaseException):
    """The Sparse Solver Module is not licensed."""

    pass


class ERR7_StageDoesNotExist(St7BaseException):
    """The specified stage does not exist."""

    pass


class ERR7_TJunctionsFound(St7BaseException):
    """The selected plate hull contains t-junctions."""

    pass


class ERR7_TableDoesNotExist(St7BaseException):
    """The specified table does not exist."""

    pass


class ERR7_TableNameAlreadyExists(St7BaseException):
    """The specified table already exists."""

    pass


class ERR7_TableTypeIsNotTimeBased(St7BaseException):
    """The specified table is not time based."""

    pass


class ERR7_TooManyAnimations(St7BaseException):
    """Maximum number of animations are already running."""

    pass


class ERR7_TooManyBeamStations(St7BaseException):
    """Too many beam stations were specified."""

    pass


class ERR7_UCSIDAlreadyExists(St7BaseException):
    """The UCS ID already exists."""

    pass


class ERR7_UCSMustBeDifferent(St7BaseException):
    """UCS1 and UCS2 must be different."""

    pass


class ERR7_UnexpectedSolverTermination(St7BaseException):
    """The solver terminated unexpectedly."""

    pass


class ERR7_UnknownError(St7BaseException):
    """An unknown error has occured."""

    pass


class ERR7_UnknownFileType(St7BaseException):
    """The type of the specified file is unknown."""

    pass


class ERR7_UnknownProperty(St7BaseException):
    """Unknown property number."""

    pass


class ERR7_UnknownResultLocation(St7BaseException):
    """The result location is not valid."""

    pass


class ERR7_UnknownResultType(St7BaseException):
    """The result type is not valid."""

    pass


class ERR7_UnknownSolver(St7BaseException):
    """The specified solver type is not valid."""

    pass


class ERR7_UnknownSubType(St7BaseException):
    """Unknown result subtype."""

    pass


class ERR7_UnknownSurfaceLocation(St7BaseException):
    """The surface location is not valid."""

    pass


class ERR7_UnknownTitle(St7BaseException):
    """Unknown title."""

    pass


class ERR7_YieldNotMCDP(St7BaseException):
    """The yield criterion for the specified property is not Mohr-Coulomb or Drucker-Prager."""

    pass


class SE_ActiveStageHasNoIncrements(St7BaseException):
    """Solver Error: Load increments are not defined for an active stage."""

    pass


class SE_AttachmentsInWrongGroup(St7BaseException):
    """
    Solver Error: One or more attachment links are active in stages where their targets are inactive.
    """

    pass


class SE_BadTaperData(St7BaseException):
    """Solver Error: Beam element has invalid taper attributes."""

    pass


class SE_BeamPoissonOutOfRange(St7BaseException):
    """
    Solver Error: Effective Poisson's ratio for beam property is not valid because a nonlinear stress-
    strain table is used.
    """

    pass


class SE_BeamPropertiesMayHaveChanged(St7BaseException):
    """Solver Error: Beam property discretisation may have changed."""

    pass


class SE_BeamRequiresPoisson(St7BaseException):
    """
    Solver Error: Beam property needs a valid Poisson's ratio because it uses a nonlinear stress-strain
    table.
    """

    pass


class SE_CQCRequiresDamping(St7BaseException):
    """Solver Error: Spectral CQC results require damping."""

    pass


class SE_CableRequiresGNL(St7BaseException):
    """Solver Error: Cable elements require the geometry nonlinear option."""

    pass


class SE_CableRequiresNonlinearSolver(St7BaseException):
    """Solver Error: Cable elements require a nonlinear solver."""

    pass


class SE_CannotAppendToFile(St7BaseException):
    """Solver Error: Cannot append to file."""

    pass


class SE_CannotConvertAttachmentLink(St7BaseException):
    """Solver Error: Attachment link is not valid as it generates a singular matrix."""

    pass


class SE_CannotConvertInterpMultiPoint(St7BaseException):
    """Solver Error: Multipoint link generated a singlular matrix."""

    pass


class SE_CannotFindSolver(St7BaseException):
    """Solver Error: Cannot find solver."""

    pass


class SE_CannotOverwriteFile(St7BaseException):
    """Solver Error: Cannot overwrite file."""

    pass


class SE_CannotReadRestartFile(St7BaseException):
    """Solver Error: Cannot read restart file."""

    pass


class SE_CannotReadWriteScratchPath(St7BaseException):
    """
    Solver Error: The scratch path does not have sufficient read/write access to allow the solver to
    run.
    """

    pass


class SE_CannotWriteToLogFile(St7BaseException):
    """Solver Error: Cannot write to log file."""

    pass


class SE_CannotWriteToResultFile(St7BaseException):
    """Solver Error: Cannot write to result file."""

    pass


class SE_CompositesModuleNotLicensed(St7BaseException):
    """Solver Error: The Composites Module is not licensed."""

    pass


class SE_ConcreteCreepMNL(St7BaseException):
    """
    Solver Error: Concrete creep and material stress-strain tables cannot be considered together.
    """

    pass


class SE_CreepTimeTooShort(St7BaseException):
    """Solver Error: Creep curve fit time is too short."""

    pass


class SE_DuplicateLinks(St7BaseException):
    """Solver Error: Duplicate links in model."""

    pass


class SE_ElementUsesInvalidProperty(St7BaseException):
    """Solver Error: An element uses an invalid property."""

    pass


class SE_HarmonicFactorsAllZero(St7BaseException):
    """Solver Error: Harmonic factors are all zero."""

    pass


class SE_HaveLinearCables(St7BaseException):
    """Solver Error: Initial conditions not valid for selected case due to cables."""

    pass


class SE_InactiveCavityControlCase(St7BaseException):
    """Solver Error: Cavities with inactive pressure control cases were found"""

    pass


class SE_IncompatibleRestartFile(St7BaseException):
    """Solver Error: Incompatible restart file."""

    pass


class SE_IncompatibleRestartUnits(St7BaseException):
    """
    Solver Error: The units in the result file selected for appending are different to the units in the
    model.
    """

    pass


class SE_InitialConditionsNotValid(St7BaseException):
    """Solver Error: Initial conditions are not valid."""

    pass


class SE_InitialSolutionFileIsBad(St7BaseException):
    """Solver Error: The file used in the initial analysis cannot be found or is not valid."""

    pass


class SE_InsufficientRestartFileSteps(St7BaseException):
    """
    Solver Error: The restart file contains fewer result cases than the requested restart case.
    """

    pass


class SE_InvalidBrickCohesionValue(St7BaseException):
    """Solver Error: Invalid brick cohesion value."""

    pass


class SE_InvalidBrickShrinkageDefinition(St7BaseException):
    """Solver Error: The creep/shrinkage definition required by a brick property is not valid."""

    pass


class SE_InvalidCavityFluidDefinition(St7BaseException):
    """Solver Error: Invalid fluid cavities were found"""

    pass


class SE_InvalidDirectionVector(St7BaseException):
    """Solver Error: Invalid direction vector."""

    pass


class SE_InvalidElement(St7BaseException):
    """Solver Error: Model contains an invalid element."""

    pass


class SE_InvalidElements(St7BaseException):
    """Solver Error: Elements with invalid connections were found."""

    pass


class SE_InvalidFrequencyRange(St7BaseException):
    """Solver Error: Invalid frequency range."""

    pass


class SE_InvalidGravityCase(St7BaseException):
    """Solver Error: The load case selected as the soil/fluid gravity case is not valid."""

    pass


class SE_InvalidInitialFile(St7BaseException):
    """Solver Error: Invalid initial file."""

    pass


class SE_InvalidInitialTemperatureFile(St7BaseException):
    """Solver Error: Invalid initial temperature file."""

    pass


class SE_InvalidLaminateID(St7BaseException):
    """Solver Error: A plate property references an invalid laminate definition."""

    pass


class SE_InvalidLink(St7BaseException):
    """Solver Error: Model contains an invalid link."""

    pass


class SE_InvalidMaterialNonlinearString(St7BaseException):
    """
    Solver Error: For material nonlinearity, all elements in a string group must use the same property
    set.
    """

    pass


class SE_InvalidPlateCohesionValue(St7BaseException):
    """Solver Error: Invalid plate cohesion value."""

    pass


class SE_InvalidPlateShrinkageDefinition(St7BaseException):
    """Solver Error: The creep/shrinkage definition required by a plate property is not valid."""

    pass


class SE_InvalidPlateVariableRequested(St7BaseException):
    """Solver Error: Plate{s} have one or more invalid response variables assigned."""

    pass


class SE_InvalidPreTensionOnString(St7BaseException):
    """Solver Error: A string group with variable pre-tension was found."""

    pass


class SE_InvalidRayleighFactors(St7BaseException):
    """Solver Error: Invalid Rayleigh factors."""

    pass


class SE_InvalidRestartFile(St7BaseException):
    """Solver Error: Invalid restart file."""

    pass


class SE_InvalidSolverResultFile(St7BaseException):
    """Solver Error: Invalid solver result file."""

    pass


class SE_InvalidStringGroupDefinition(St7BaseException):
    """Solver Error: An invalid string group was found."""

    pass


class SE_InvalidTimeStep(St7BaseException):
    """Solver Error: Invalid time steps used in model."""

    pass


class SE_InvalidUserBrickCreepDefinition(St7BaseException):
    """Solver Error: The user defined creep table required by a brick property is not valid."""

    pass


class SE_InvalidUserPlateCreepDefinition(St7BaseException):
    """Solver Error: The user defined creep table required by a plate property is not valid."""

    pass


class SE_LinksHaveNoFreedomCase(St7BaseException):
    """
    Solver Error: Shrink, 2-Point and/or User-MPL links without Control Freedom Cases were found.
    """

    pass


class SE_LoadIncrementsNotDefined(St7BaseException):
    """Solver Error: Load increments not defined."""

    pass


class SE_MissingInsituStress(St7BaseException):
    """Solver Error: Some soil elements do not have in-situ stress attributes."""

    pass


class SE_ModelMixesAxiNonAxi(St7BaseException):
    """Solver Error: Model mixes axisymmetric elements with non-axisymmetric elements."""

    pass


class SE_MoreLoadIncrementsNeeded(St7BaseException):
    """Solver Error: More load increments are required."""

    pass


class SE_MovingLoadModuleNotLicensed(St7BaseException):
    """Solver Error: The Moving Load Module is not licensed."""

    pass


class SE_NeedElementNodeForce(St7BaseException):
    """
    Solver Error: Element Node Force option is required to consider reaction multi-point links.
    """

    pass


class SE_NeedNodeTempNTASolver(St7BaseException):
    """
    Solver Error: Table Type nodal temperatures are not supported by the linear transient dynamic
    solver.
    """

    pass


class SE_NeedNonlinearHeatSolver(St7BaseException):
    """Solver Error: Model requires the nonlinear heat solver."""

    pass


class SE_NeedTemperatureTables(St7BaseException):
    """
    Solver Error: This model contains temperature dependent material properties, which are ignored by
    the current solver settings.
    """

    pass


class SE_NoBeamProperties(St7BaseException):
    """Solver Error: No beam properties defined."""

    pass


class SE_NoBrickProperties(St7BaseException):
    """Solver Error: No brick properties defined."""

    pass


class SE_NoFreedomCaseInIncrements(St7BaseException):
    """Solver Error: No freedom case in increments."""

    pass


class SE_NoFreedomCaseSelected(St7BaseException):
    """Solver Error: No freedom case selected."""

    pass


class SE_NoLoadCaseSelected(St7BaseException):
    """Solver Error: No load case selected."""

    pass


class SE_NoLoadTablesDefined(St7BaseException):
    """Solver Error: No load tables defined."""

    pass


class SE_NoModesIncluded(St7BaseException):
    """Solver Error: No modes included."""

    pass


class SE_NoMovingLoadPathsInCases(St7BaseException):
    """Solver Error: No load paths were found in the selected load cases."""

    pass


class SE_NoNodes(St7BaseException):
    """Solver Error: The model must contain at least one node to run the solver."""

    pass


class SE_NoPlateProperties(St7BaseException):
    """Solver Error: No plate properties defined."""

    pass


class SE_NoResponseVariablesDefined(St7BaseException):
    """Solver Error: No response variables (entity attributes) have been defined."""

    pass


class SE_NoSpectralResultsSelected(St7BaseException):
    """Solver Error: No spectral results selected."""

    pass


class SE_NoTimeStepsSaved(St7BaseException):
    """Solver Error: No time steps are saved."""

    pass


class SE_NoVelocityDataInInitialFile(St7BaseException):
    """Solver Error: No velocity data in initial file."""

    pass


class SE_NonlinearSolverRequired(St7BaseException):
    """Solver Error: Model requires the nonlinear solver."""

    pass


class SE_RubberRequiresGNL(St7BaseException):
    """Solver Error: Rubber material in model requires the geometry nonlinear option."""

    pass


class SE_ShearPanelMustBeQuad4(St7BaseException):
    """Solver Error: Shear panel must be Quad4."""

    pass


class SE_SingleShotRestartFile(St7BaseException):
    """Solver Error: The restart file contains only the last saved result case."""

    pass


class SE_SingularBrickMatrix(St7BaseException):
    """Solver Error: Singular brick matrix."""

    pass


class SE_SingularPlateMatrix(St7BaseException):
    """Solver Error: Singular plate matrix."""

    pass


class SE_SkylineUsesBadSort(St7BaseException):
    """
    Solver Error: The Skyline scheme usually works best with the Tree and Geometry node orderings.
    """

    pass


class SE_SoilRequiresMNL(St7BaseException):
    """Solver Error: Soil material in model requires the material nonlinear option."""

    pass


class SE_SpectralBaseExcitationsAllZero(St7BaseException):
    """Solver Error: All spectral base excitations are zero."""

    pass


class SE_SpectralCasesNotDefined(St7BaseException):
    """Solver Error: No spectral base or load excitations are defined."""

    pass


class SE_SpectralExcitationsAllZero(St7BaseException):
    """Solver Error: All spectral excitations are zero."""

    pass


class SE_SpectralLoadExcitationsAllZero(St7BaseException):
    """Solver Error: All spectral load excitations are zero."""

    pass


class SE_StagedSolutionFileNotFound(St7BaseException):
    """
    Solver Error: The file used in the initial staged analysis cannot be found or is not valid.
    """

    pass


class SE_StagingHasChanged(St7BaseException):
    """
    Solver Error: Stage definitions in the initial file are not compatible with the current stage
    definitions in this model.
    """

    pass


class SE_StringOrderHasChanged(St7BaseException):
    """
    Solver Error: The string elements defined in the model are not compatible with those in the restart
    file.
    """

    pass


class SE_TableNotFound(St7BaseException):
    """Solver Error: A table specified in the model was not found."""

    pass


class SE_TaperedPlasticBeams(St7BaseException):
    """Solver Error: Tapered beams do not support material nonlinearity."""

    pass


class SE_TemperatureDependenceCaseNotSet(St7BaseException):
    """Solver Error: Temperature dependence case is not set."""

    pass


class SE_TensileInsituBrickStress(St7BaseException):
    """
    Solver Error: Some soil elements (bricks) have tensile (positive) in-situ stress attributes.
    """

    pass


class SE_TensileInsituPlateStress(St7BaseException):
    """
    Solver Error: Some soil elements (plates) have tensile (positive) in-situ stress attributes.
    """

    pass


class SE_UnknownException(St7BaseException):
    """Solver Error: Unknown error."""

    pass


class SE_ZeroLengthRigidLinkGenerated(St7BaseException):
    """Solver Error: A link of zero length was generated."""

    pass


class ST_Abnormal(St7BaseException):
    """ST_Abnormal"""

    pass


class ST_CreateLog(St7BaseException):
    """ST_CreateLog"""

    pass


class ST_Internal(St7BaseException):
    """ST_Internal"""

    pass


class ST_MemError(St7BaseException):
    """ST_MemError"""

    pass


class ST_NoDisk(St7BaseException):
    """ST_NoDisk"""

    pass


class ST_NoError(St7BaseException):
    """ST_NoError"""

    pass


class ST_NoLicence(St7BaseException):
    """ST_NoLicence"""

    pass


class ST_NoRam(St7BaseException):
    """ST_NoRam"""

    pass


class ST_OpenLog(St7BaseException):
    """ST_OpenLog"""

    pass


class ST_Scratch(St7BaseException):
    """ST_Scratch"""

    pass


class ST_UserStop(St7BaseException):
    """ST_UserStop"""

    pass


class ST_WriteLog(St7BaseException):
    """ST_WriteLog"""

    pass


_err_dict = {
    -12: ERR7_APIAlreadyInitialised,
    -11: ERR7_LoginExceeded,
    -10: ERR7_CannotCommunicate,
    -9: ERR7_CannotFindNetworkLock,
    -8: ERR7_CannotFindStandaloneLock,
    -7: ERR7_CannotInitialiseDirectX,
    -6: ERR7_InvalidRegionalSettings,
    -5: ERR7_InvalidDLLsPresent,
    -4: ERR7_APINotInitialised,
    -3: ERR7_InvalidErrorCode,
    -2: ERR7_APIModuleNotLicensed,
    -1: ERR7_UnknownError,
    0: ERR7_NoError,
    1: ERR7_FileAlreadyOpen,
    2: ERR7_FileNotFound,
    3: ERR7_FileNotSt7,
    4: ERR7_InvalidFileName,
    5: ERR7_FileIsNewer,
    6: ERR7_CannotReadFile,
    7: ERR7_InvalidScratchPath,
    8: ERR7_FileNotOpen,
    9: ERR7_ExceededTotal,
    10: ERR7_DataNotFound,
    11: ERR7_InvalidResultFile,
    12: ERR7_ResultFileNotOpen,
    13: ERR7_ExceededResultCase,
    14: ERR7_UnknownResultType,
    15: ERR7_UnknownResultLocation,
    16: ERR7_UnknownSurfaceLocation,
    17: ERR7_UnknownProperty,
    18: ERR7_InvalidEntity,
    19: ERR7_InvalidBeamPosition,
    20: ERR7_InvalidLoadCase,
    21: ERR7_InvalidFreedomCase,
    22: ERR7_UnknownTitle,
    23: ERR7_InvalidResOptsNFADisp,
    24: ERR7_TooManyBeamStations,
    25: ERR7_UnknownSubType,
    26: ERR7_GroupIdDoesNotExist,
    27: ERR7_InvalidFileUnit,
    28: ERR7_CannotSaveFile,
    29: ERR7_ResultFileIsOpen,
    30: ERR7_InvalidUnits,
    31: ERR7_InvalidEntityNodes,
    32: ERR7_InvalidUCSType,
    33: ERR7_InvalidUCSID,
    34: ERR7_UCSIDAlreadyExists,
    35: ERR7_CaseNameAlreadyExists,
    36: ERR7_InvalidEntityNumber,
    37: ERR7_InvalidBeamEnd,
    38: ERR7_InvalidBeamDir,
    39: ERR7_InvalidPlateEdge,
    40: ERR7_InvalidBrickFace,
    41: ERR7_InvalidBeamType,
    42: ERR7_InvalidPlateType,
    43: ERR7_InvalidMaterialType,
    44: ERR7_PropertyAlreadyExists,
    45: ERR7_InvalidBeamSectionType,
    46: ERR7_PropertyNotSpring,
    47: ERR7_PropertyNotCable,
    48: ERR7_PropertyNotTruss,
    49: ERR7_PropertyNotCutOffBar,
    50: ERR7_PropertyNotPointContact,
    51: ERR7_PropertyNotBeam,
    52: ERR7_PropertyNotPipe,
    53: ERR7_PropertyNotConnectionBeam,
    54: ERR7_InvalidSectionParameters,
    55: ERR7_PropertyNotUserDefinedBeam,
    56: ERR7_MaterialIsUserDefined,
    57: ERR7_MaterialNotIsotropic,
    58: ERR7_MaterialNotOrthotropic,
    59: ERR7_InvalidRubberModel,
    60: ERR7_MaterialNotRubber,
    61: ERR7_InvalidSectionProperties,
    62: ERR7_PlateDoesNotHaveThickness,
    63: ERR7_IncompatibleMaterialCombination,
    64: ERR7_UnknownSolver,
    65: ERR7_InvalidSolverMode,
    66: ERR7_InvalidMirrorOption,
    67: ERR7_SectionCannotBeMirrored,
    68: ERR7_InvalidTableType,
    69: ERR7_InvalidTableName,
    70: ERR7_TableNameAlreadyExists,
    71: ERR7_InvalidNumberOfEntries,
    72: ERR7_InvalidToleranceType,
    73: ERR7_TableDoesNotExist,
    74: ERR7_NotFrequencyTable,
    75: ERR7_InvalidFrequencyType,
    76: ERR7_InvalidTableSetting,
    77: ERR7_IncompatibleTableType,
    78: ERR7_IncompatibleCriterionCombination,
    79: ERR7_InvalidModalFile,
    80: ERR7_InvalidCombinationCaseNumber,
    81: ERR7_InvalidInitialCaseNumber,
    82: ERR7_InvalidInitialFile,
    83: ERR7_InvalidModeNumber,
    84: ERR7_BeamIsNotBXS,
    85: ERR7_InvalidDampingType,
    86: ERR7_InvalidRayleighMode,
    87: ERR7_CannotReadBXS,
    88: ERR7_InvalidResultType,
    89: ERR7_InvalidSolverParameter,
    90: ERR7_InvalidModalLoadType,
    91: ERR7_InvalidTimeRow,
    92: ERR7_SparseSolverModuleNotLicensed,
    93: ERR7_InvalidSolverScheme,
    94: ERR7_InvalidSortOption,
    95: ERR7_IncompatibleResultFile,
    96: ERR7_InvalidLinkType,
    97: ERR7_InvalidLinkData,
    98: ERR7_OnlyOneLoadCase,
    99: ERR7_OnlyOneFreedomCase,
    100: ERR7_InvalidLoadID,
    101: ERR7_InvalidBeamLoadType,
    102: ERR7_InvalidStringID,
    103: ERR7_InvalidPatchType,
    104: ERR7_IncrementDoesNotExist,
    105: ERR7_InvalidLoadCaseType,
    106: ERR7_InvalidFreedomCaseType,
    107: ERR7_InvalidHarmonicLoadType,
    108: ERR7_InvalidTemperatureType,
    109: ERR7_InvalidPatchTypeForPlate,
    110: ERR7_InvalidAttributeType,
    111: ERR7_MaterialNotAnisotropic,
    112: ERR7_InvalidMatrixType,
    113: ERR7_MaterialNotUserDefined,
    114: ERR7_InvalidIndex,
    115: ERR7_InvalidContactType,
    116: ERR7_InvalidContactSubType,
    117: ERR7_InvalidCutoffType,
    118: ERR7_ResultQuantityNotAvailable,
    119: ERR7_YieldNotMCDP,
    120: ERR7_CombinationDoesNotExist,
    121: ERR7_InvalidSeismicCase,
    122: ERR7_InvalidImportExportMode,
    123: ERR7_CannotReadImportFile,
    124: ERR7_InvalidAnsysImportFormat,
    125: ERR7_InvalidAnsysArrayStatus,
    126: ERR7_CannotWriteExportFile,
    127: ERR7_InvalidAnsysExportFormat,
    128: ERR7_InvalidAnsysEndReleaseOption,
    129: ERR7_InvalidAnsysExportUnits,
    130: ERR7_InvalidSt7ExportFormat,
    131: ERR7_InvalidUVPos,
    132: ERR7_InvalidResponseType,
    133: ERR7_InvalidLayoutID,
    134: ERR7_InvalidPlateSurface,
    135: ERR7_MeshingErrors,
    136: ERR7_InvalidTolerance,
    137: ERR7_InvalidTaperAxis,
    138: ERR7_InvalidTaperType,
    139: ERR7_InvalidTaperRatio,
    140: ERR7_InvalidPositionType,
    141: ERR7_InvalidPreLoadType,
    142: ERR7_InvalidVertexType,
    143: ERR7_InvalidVertexMeshSize,
    144: ERR7_InvalidGeometryEdgeType,
    145: ERR7_InvalidPropertyNumber,
    146: ERR7_InvalidFaceSurface,
    147: ERR7_InvalidModType,
    148: ERR7_MaterialNotSoil,
    149: ERR7_MaterialNotFluid,
    150: ERR7_SoilTypeNotDC,
    151: ERR7_SoilTypeNotCC,
    152: ERR7_MaterialNotLaminate,
    153: ERR7_InvalidLaminateID,
    154: ERR7_LaminateNameAlreadyExists,
    155: ERR7_LaminateIDAlreadyExists,
    156: ERR7_PlyDoesNotExist,
    157: ERR7_ExceededMaxNumPlies,
    158: ERR7_LayoutIDAlreadyExists,
    159: ERR7_InvalidNumModes,
    160: ERR7_InvalidLTAMethod,
    161: ERR7_InvalidLTASolutionType,
    162: ERR7_ExceededMaxNumStages,
    163: ERR7_StageDoesNotExist,
    164: ERR7_ExceededMaxNumSpectralCases,
    165: ERR7_InvalidSpectralCase,
    166: ERR7_InvalidSpectrumType,
    167: ERR7_InvalidResultsSign,
    168: ERR7_InvalidPositionTableAxis,
    169: ERR7_InvalidInitialConditionsType,
    170: ERR7_ExceededMaxNumNodeHistory,
    171: ERR7_NodeHistoryDoesNotExist,
    172: ERR7_InvalidTransientTempType,
    173: ERR7_InvalidTimeUnit,
    174: ERR7_InvalidLoadPath,
    175: ERR7_InvalidTempDependenceType,
    176: ERR7_InvalidTrigType,
    177: ERR7_InvalidUserEquation,
    178: ERR7_InvalidCreepID,
    179: ERR7_CreepIDAlreadyExists,
    180: ERR7_InvalidCreepLaw,
    181: ERR7_InvalidCreepHardeningLaw,
    182: ERR7_InvalidCreepViscoChainRow,
    183: ERR7_InvalidCreepFunctionType,
    184: ERR7_InvalidCreepShrinkageType,
    185: ERR7_InvalidTableRow,
    186: ERR7_ExceededMaxNumRows,
    187: ERR7_InvalidLoadPathTemplateID,
    188: ERR7_LoadPathTemplateIDAlreadyExists,
    189: ERR7_InvalidLoadPathLane,
    190: ERR7_ExceededMaxNumLoadPathTemplates,
    191: ERR7_ExceededMaxNumLoadPathVehicles,
    192: ERR7_InvalidLoadPathVehicle,
    193: ERR7_InvalidMobilityType,
    194: ERR7_InvalidAxisSystem,
    195: ERR7_InvalidLoadPathID,
    196: ERR7_LoadPathIDAlreadyExists,
    197: ERR7_InvalidPathDefinition,
    198: ERR7_InvalidLoadPathShape,
    199: ERR7_InvalidLoadPathSurface,
    200: ERR7_InvalidNumPathDivs,
    201: ERR7_InvalidGeometryCavityLoop,
    202: ERR7_InvalidLimitEnvelope,
    203: ERR7_ExceededMaxNumLimitEnvelopes,
    204: ERR7_InvalidCombEnvelope,
    205: ERR7_ExceededMaxNumCombEnvelopes,
    206: ERR7_InvalidFactorsEnvelope,
    207: ERR7_ExceededMaxNumFactorsEnvelopes,
    208: ERR7_InvalidLimitEnvelopeType,
    209: ERR7_InvalidCombEnvelopeType,
    210: ERR7_InvalidFactorsEnvelopeType,
    211: ERR7_InvalidCombEnvelopeAccType,
    212: ERR7_InvalidEnvelopeSet,
    213: ERR7_ExceededMaxNumEnvelopeSets,
    214: ERR7_InvalidEnvelopeSetType,
    215: ERR7_InvalidCombResFile,
    216: ERR7_ExceededMaxNumCombResFiles,
    217: ERR7_CannotCombResFiles,
    218: ERR7_InvalidStartEndTimes,
    219: ERR7_InvalidNumSteps,
    220: ERR7_InvalidLibraryPath,
    221: ERR7_InvalidLibraryType,
    222: ERR7_InvalidLibraryID,
    223: ERR7_InvalidLibraryName,
    224: ERR7_InvalidLibraryItemID,
    225: ERR7_InvalidLibraryItemName,
    226: ERR7_InvalidDisplayOptionsPath,
    227: ERR7_InvalidSolverPath,
    228: ERR7_InvalidCementHardeningType,
    229: ERR7_NoPlateElements,
    230: ERR7_CannotMakeBXS,
    231: ERR7_CannotCalculateBXSData,
    232: ERR7_InvalidSurfaceMeshTargetType,
    233: ERR7_InvalidModalNodeReactType,
    234: ERR7_InvalidAxis,
    235: ERR7_InvalidBeamAxisType,
    236: ERR7_InvalidStaadCountryCodeOption,
    237: ERR7_InvalidGeometryFormatProtocol,
    238: ERR7_InvalidDXFBeamOption,
    239: ERR7_InvalidDXFPlateOption,
    240: ERR7_InvalidLoadPathLaneFactorType,
    241: ERR7_InvalidLoadPathVehicleInstance,
    242: ERR7_InvalidNumBeamStations,
    243: ERR7_ResFileUnsupportedType,
    244: ERR7_ResFileAlreadyOpen,
    245: ERR7_ResFileInvalidNumCases,
    246: ERR7_ResFileNotOpen,
    247: ERR7_ResFileInvalidCase,
    248: ERR7_ResFileDoesNotHaveEntity,
    249: ERR7_ResFileInvalidQuantity,
    250: ERR7_ResFileQuantityNotExist,
    251: ERR7_ResFileCantSave,
    252: ERR7_ResFileCantClearQuantity,
    253: ERR7_ResFileContainsNoElements,
    254: ERR7_ResFileContainsNoNodes,
    255: ERR7_InvalidName,
    256: ERR7_ResFileAssociationNotAllowed,
    257: ERR7_ResFileIncompatibleQuantity,
    258: ERR7_CannotEditSolverFiles,
    259: ERR7_CannotOpenResultFile,
    260: ERR7_CouldNotShowModelWindow,
    261: ERR7_ModelWindowWasNotShowing,
    262: ERR7_CantDoWithModalWindows,
    263: ERR7_InvalidSelectionEndEdgeFace,
    264: ERR7_CouldNotCreateModelWindow,
    265: ERR7_ModelWindowWasNotCreated,
    266: ERR7_InvalidImageType,
    267: ERR7_InvalidImageDimensions,
    268: ERR7_ErrorCreatingImage,
    269: ERR7_CannotSaveImageFile,
    270: ERR7_InvalidWindowDimensions,
    271: ERR7_InvalidResultQuantity,
    272: ERR7_InvalidResultSubQuantity,
    273: ERR7_InvalidComponent,
    274: ERR7_ResultIsNotAvailable,
    275: ERR7_InvalidUCSIndex,
    276: ERR7_InvalidDiagramAxis,
    277: ERR7_InvalidVectorComponents,
    278: ERR7_TableTypeIsNotTimeBased,
    279: ERR7_InvalidTableID,
    280: ERR7_LinkNotMasterSlave,
    281: ERR7_LinkNotSectorSymmetry,
    282: ERR7_LinkNotCoupling,
    283: ERR7_LinkNotPinned,
    284: ERR7_LinkNotRigid,
    285: ERR7_LinkNotShrink,
    286: ERR7_LinkNotTwoPoint,
    287: ERR7_LinkNotAttachment,
    288: ERR7_LinkNotMultiPoint,
    289: ERR7_InvalidCoupleType,
    290: ERR7_InvalidRigidPlane,
    291: ERR7_InvalidMultiPointType,
    292: ERR7_InvalidMultiPointLink,
    293: ERR7_InvalidAttachmentType,
    294: ERR7_ExceededMaxNumColumns,
    295: ERR7_CouldNotDestroyModelWindow,
    296: ERR7_CannotSetWindowParent,
    297: ERR7_InvalidLoadCaseFilePath,
    298: ERR7_InvalidStaadLengthUnit,
    299: ERR7_InvalidStaadForceUnit,
    300: ERR7_InvalidDuplicateFaceType,
    301: ERR7_InvalidNodeCoordinateKeepType,
    302: ERR7_CommentDoesNotExist,
    303: ERR7_InvalidFilePath,
    304: ERR7_InvalidContactYieldType,
    305: ERR7_InvalidNumMeshingLoops,
    306: ERR7_InvalidMeshPositionOnUCS,
    307: ERR7_InvalidK0Expression,
    308: ERR7_InvalidK1Expression,
    309: ERR7_InvalidNumCopies,
    310: ERR7_InvalidCurvedPipesAsOption,
    311: ERR7_InvalidResOptsRotationUnit,
    312: ERR7_RayleighNotApplicable,
    313: ERR7_InvalidAttributeSetting,
    314: ERR7_InvalidToolOptsZipOptions,
    315: ERR7_InvalidToolOptsSubdivideOptions,
    316: ERR7_InvalidToolOptsCopyOptions,
    317: ERR7_InvalidBackgroundMode,
    318: ERR7_InvalidAttachPartsParams,
    319: ERR7_InvalidDrawParameters,
    320: ERR7_FilesStillOpen,
    321: ERR7_SolverStillRunning,
    322: ERR7_InvalidFaceFromBeamPolygonParameters,
    323: ERR7_InvalidResOptsStrainUnit,
    324: ERR7_FunctionNotSupported,
    325: ERR7_SoilTypeNotMC,
    326: ERR7_SoilTypeNotDP,
    327: ERR7_TooManyAnimations,
    328: ERR7_InvalidAnimationFile,
    329: ERR7_InvalidAnimationMode,
    330: ERR7_InsufficientFrames,
    331: ERR7_AnimationDimensionsTooSmall,
    332: ERR7_AnimationDimensionsTooLarge,
    333: ERR7_ReducedAnimation,
    334: ERR7_InvalidAnimationType,
    335: ERR7_InvalidEntityID,
    336: ERR7_CouldNotSaveAnimationFile,
    337: ERR7_AnimationHandleOutOfRange,
    338: ERR7_AnimationNotRunning,
    339: ERR7_SoilTypeNotLS,
    340: ERR7_InvalidPlane,
    341: ERR7_InvalidAlphaTempType,
    342: ERR7_InvalidGravityDirection,
    343: ERR7_InvalidAttachmentDirection,
    344: ERR7_InvalidHardeningType,
    345: ERR7_ResultCaseNotInertiaRelief,
    346: ERR7_InvalidNumLayers,
    347: ERR7_PlateDoesNotHaveLayers,
    348: ERR7_OperationFailed,
    349: ERR7_InvalidEntityContourFileType,
    350: ERR7_InvalidBrickIntegrationPoints,
    351: ERR7_InvalidDirection,
    352: ERR7_InvalidAttachConnectionType,
    353: ERR7_CannotSaveIniFile,
    354: ERR7_InvalidDivisionParameters,
    355: ERR7_InvalidContourIndex,
    356: ERR7_InvalidProjectFlag,
    357: ERR7_InvalidSegmentsPerCircle,
    358: ERR7_InvalidArcLength,
    359: ERR7_InvalidDivisionTargets,
    360: ERR7_InvalidProcessingMode,
    361: ERR7_InvalidDigits,
    362: ERR7_InvalidNumericStyle,
    363: ERR7_InvalidExponentFormat,
    364: ERR7_InvalidExportParameters,
    365: ERR7_InsituCalculationFailed,
    366: ERR7_ModelMixesAxiNonAxi,
    367: ERR7_InvalidInsituRunMode,
    368: ERR7_InvalidGradeType,
    369: ERR7_InvalidGradeRatio,
    370: ERR7_InvalidSplitData,
    371: ERR7_CannotMorphEdges,
    372: ERR7_TJunctionsFound,
    373: ERR7_FreeEdgesFound,
    374: ERR7_InvalidSTLFileFormat,
    375: ERR7_InvalidSTLGroupingOption,
    376: ERR7_InvalidSTLBeamOption,
    377: ERR7_InvalidSTLPlateOption,
    378: ERR7_InvalidNodeExtrudeTarget,
    379: ERR7_InvalidBeamExtrudeTarget,
    380: ERR7_InvalidLinkTarget,
    381: ERR7_InvalidSourceAction,
    382: ERR7_InvalidLinePoints,
    383: ERR7_InvalidLineID,
    384: ERR7_InvalidPlanePoints,
    385: ERR7_InvalidPlaneID,
    386: ERR7_InvalidSortMethod,
    387: ERR7_InvalidDirectionVector,
    388: ERR7_InvalidRCLayers,
    389: ERR7_InvalidConnectionType,
    390: ERR7_InvalidQuadraticAsOption,
    391: ERR7_InvalidGeometryAsOption,
    392: ERR7_InvalidSplitRatio,
    393: ERR7_InvalidLength,
    394: ERR7_InvalidEdgeTolerance,
    395: ERR7_InvalidRadius,
    396: ERR7_IncompatibleSections,
    397: ERR7_UCSMustBeDifferent,
    398: ERR7_InvalidNumCutFaces,
    399: ERR7_InvalidNumRepeats,
    400: ERR7_InvalidP1P2,
    401: ERR7_InvalidP1P2P3,
    402: ERR7_InvalidP1P2P3P4,
    403: ERR7_IntersectionNotFound,
    404: ERR7_CantGenerateFillet,
    405: ERR7_InvalidR1R2,
    406: ERR7_InvalidR2,
    407: ERR7_InvalidPLTarget,
    408: ERR7_InvalidScaleAbout,
    409: ERR7_InvalidProjectionDirection,
    410: ERR7_InvalidCollectionID,
    411: ERR7_InvalidDivisions,
    412: ERR7_InvalidLineDefinition,
    413: ERR7_InvalidOriginMethod,
    414: ERR7_InvalidInfluenceFile,
    415: ERR7_InvalidResponseVariable,
    416: ERR7_NoMultiVariableInfluenceCases,
    417: ERR7_InvalidMultiVariableCaseID,
    418: ERR7_InvalidMultiVariableType,
    419: ERR7_NoInfluenceCombinationsDefined,
    420: ERR7_NothingSelected,
    421: ERR7_InvalidPasteOption,
    422: ERR7_InvalidResultCase,
    423: ERR7_InvalidEntitySet,
    424: ERR7_InvalidResOptsReactionLinkGNL,
    425: ERR7_FileIsProtected,
    426: ERR7_InvalidHRAMode,
    427: ERR7_InvalidBGLData,
    428: ERR7_InvalidWindowMode,
    429: ERR7_UnexpectedSolverTermination,
    430: ERR7_InvalidReferenceNode,
    431: ERR7_InvalidDetachMode,
    432: ERR7_InvalidResOptsBaseMode,
    433: ERR7_InvalidMarkerType,
    434: ERR7_InvalidMarkerStyle,
    435: ERR7_InvalidMarkerLineThickness,
    436: ERR7_InvalidMarkerSize,
    437: ERR7_MarkerNotFound,
    438: ERR7_PseudoTimeNotDefined,
    439: ERR7_EquationDoesNotExist,
    440: ERR7_InvalidOption,
    441: ERR7_InvalidIterationNumber,
    442: ERR7_InvalidAveragingOption,
    443: ERR7_InvalidContourFileIndex,
    444: ERR7_ContourFileNotLoaded,
    445: ERR7_NoLoadPathsFound,
    446: ERR7_NoElementsOnLoadPaths,
    447: ERR7_NoResponsesFound,
    448: ERR7_NoActiveResponseVariables,
    449: ERR7_NoSoilElementsFound,
    450: ERR7_OperationUserTerminated,
    451: ERR7_InvalidDefaultsMode,
    452: ERR7_InvalidFontName,
    453: ERR7_InvalidBaseExcitationType,
    454: ERR7_SectionNotBGL,
    455: ERR7_CavityFluidNotIdealGas,
    456: ERR7_CavityFluidNotConstBulk,
    457: ERR7_UnknownFileType,
    458: ERR7_FunctionalityNotAvailable,
    459: ERR7_DynamicsSolverModuleNotLicensed,
    460: ERR7_NonlinearSolverModuleNotLicensed,
    461: ERR7_MovingLoadModuleNotLicensed,
    462: ERR7_AutoMesherModuleNotLicensed,
    463: ERR7_RCModuleNotLicensed,
    464: ERR7_CompositesModuleNotLicensed,
    1001: SE_NoLoadCaseSelected,
    1002: SE_IncompatibleRestartFile,
    1003: SE_ElementUsesInvalidProperty,
    1004: SE_InvalidElement,
    1005: SE_NeedNonlinearHeatSolver,
    1006: SE_TableNotFound,
    1007: SE_InvalidRestartFile,
    1008: SE_InvalidInitialFile,
    1009: SE_InvalidSolverResultFile,
    1010: SE_InvalidLink,
    1011: SE_InvalidPlateCohesionValue,
    1012: SE_InvalidBrickCohesionValue,
    1013: SE_NonlinearSolverRequired,
    1014: SE_NoLoadTablesDefined,
    1015: SE_NoVelocityDataInInitialFile,
    1016: SE_NoModesIncluded,
    1017: SE_InvalidTimeStep,
    1018: SE_LoadIncrementsNotDefined,
    1019: SE_NoFreedomCaseInIncrements,
    1020: SE_InvalidInitialTemperatureFile,
    1021: SE_InvalidFrequencyRange,
    1022: SE_ModelMixesAxiNonAxi,
    1023: SE_CompositesModuleNotLicensed,
    1024: SE_CannotFindSolver,
    1025: SE_UnknownException,
    1026: SE_DuplicateLinks,
    1027: SE_CannotAppendToFile,
    1028: SE_CannotOverwriteFile,
    1029: SE_CannotWriteToResultFile,
    1030: SE_CannotWriteToLogFile,
    1031: SE_CannotReadRestartFile,
    1032: SE_InitialConditionsNotValid,
    1033: SE_InvalidRayleighFactors,
    1034: SE_SpectralExcitationsAllZero,
    1035: SE_ShearPanelMustBeQuad4,
    1036: SE_SingularPlateMatrix,
    1037: SE_SingularBrickMatrix,
    1038: SE_NoBeamProperties,
    1039: SE_NoPlateProperties,
    1040: SE_NoBrickProperties,
    1041: SE_MoreLoadIncrementsNeeded,
    1042: SE_RubberRequiresGNL,
    1043: SE_NoFreedomCaseSelected,
    1044: SE_SpectralCasesNotDefined,
    1045: SE_NoSpectralResultsSelected,
    1046: SE_SpectralLoadExcitationsAllZero,
    1047: SE_SpectralBaseExcitationsAllZero,
    1048: SE_NoTimeStepsSaved,
    1049: SE_InvalidDirectionVector,
    1050: SE_HarmonicFactorsAllZero,
    1051: SE_TemperatureDependenceCaseNotSet,
    1052: SE_ZeroLengthRigidLinkGenerated,
    1053: SE_InvalidStringGroupDefinition,
    1054: SE_InvalidPreTensionOnString,
    1055: SE_StringOrderHasChanged,
    1056: SE_BadTaperData,
    1057: SE_TaperedPlasticBeams,
    1058: SE_NoMovingLoadPathsInCases,
    1059: SE_NoResponseVariablesDefined,
    1060: SE_InvalidPlateVariableRequested,
    1061: SE_InvalidGravityCase,
    1062: SE_InvalidUserPlateCreepDefinition,
    1063: SE_InvalidUserBrickCreepDefinition,
    1064: SE_InvalidPlateShrinkageDefinition,
    1065: SE_InvalidBrickShrinkageDefinition,
    1066: SE_InvalidLaminateID,
    1067: SE_CannotReadWriteScratchPath,
    1068: SE_CannotConvertAttachmentLink,
    1069: SE_SoilRequiresMNL,
    1070: SE_ActiveStageHasNoIncrements,
    1071: SE_ConcreteCreepMNL,
    1072: SE_CannotConvertInterpMultiPoint,
    1073: SE_MissingInsituStress,
    1074: SE_InvalidMaterialNonlinearString,
    1075: SE_TensileInsituPlateStress,
    1076: SE_TensileInsituBrickStress,
    1077: SE_IncompatibleRestartUnits,
    1078: SE_CreepTimeTooShort,
    1079: SE_InvalidElements,
    1080: SE_InsufficientRestartFileSteps,
    1081: SE_NeedNodeTempNTASolver,
    1082: SE_SingleShotRestartFile,
    1083: SE_SkylineUsesBadSort,
    1084: SE_StagedSolutionFileNotFound,
    1085: SE_NeedTemperatureTables,
    1086: SE_AttachmentsInWrongGroup,
    1087: SE_StagingHasChanged,
    1088: SE_NoNodes,
    1089: SE_CQCRequiresDamping,
    1090: SE_HaveLinearCables,
    1091: SE_CableRequiresGNL,
    1092: SE_BeamRequiresPoisson,
    1093: SE_BeamPoissonOutOfRange,
    1094: SE_CableRequiresNonlinearSolver,
    1095: SE_InitialSolutionFileIsBad,
    1096: SE_BeamPropertiesMayHaveChanged,
    1097: SE_NeedElementNodeForce,
    1098: SE_LinksHaveNoFreedomCase,
    1099: SE_InvalidCavityFluidDefinition,
    1100: SE_InactiveCavityControlCase,
    1101: SE_MovingLoadModuleNotLicensed,
}
_solver_term_dict = {
    -11: ST_NoLicence,
    -10: ST_Scratch,
    -9: ST_MemError,
    -8: ST_WriteLog,
    -7: ST_CreateLog,
    -6: ST_OpenLog,
    -5: ST_NoRam,
    -4: ST_NoDisk,
    -3: ST_Internal,
    -2: ST_UserStop,
    -1: ST_Abnormal,
    0: ST_NoError,
}


def chk(iErr: int):
    """Checks a Strand7 error code and raised an exception which inherits from
    St7BaseException if an error code was returned."""
    if iErr == 0:
        return

    exc = _err_dict.get(iErr, St7UnknownException)

    raise exc()


def chk_st(iErr: int):
    """Checks a Strand7 error code and raised an exception which inherits from
    St7BaseException if an error code was returned."""

    if iErr == 0:
        return

    exc = _solver_term_dict.get(iErr, St7UnknownException)

    raise exc()
